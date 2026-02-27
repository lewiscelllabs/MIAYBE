#!/usr/bin/env python3
"""
miaybe_md_to_schema.py
-----------------------
Convert a MIAYBE Markdown specification file into a JSON Schema.

Usage:
    python miaybe_md_to_schema.py MIAYBE.md
    python miaybe_md_to_schema.py MIAYBE.md -o miaybe_schema.json

The script parses the MIAYBE checklist tables (sections 3.1–3.7) to extract:
  - Field IDs  (e.g. E1, C4, CC1, P1, S1, A1, PR1)
  - Field names
  - Status  (R = required, M = recommended, O = optional)
  - Definitions
  - Units (from the extra column present in CC and S tables)
  - CQ Mappings

It then assembles a JSON Schema document with the same section grouping as
MIAYBE.md and writes it to stdout or -o <file>.
"""

import re
import json
import sys
import argparse
from pathlib import Path

# ---------------------------------------------------------------------------
# Field-type hints: maps prefix → JSON type and any extras
# ---------------------------------------------------------------------------
_NUMERIC_PATTERNS = re.compile(
    r"\b(temperature|ph|dissolved|oxygen|glutamine|glucose|osmolal|co2|agitation|inoculation|culture.?volume|shaker|"
    r"collection.?timepoint|viable.?cell|viability|sample.?volume|processing.?delay|titer.?value)\b",
    re.IGNORECASE,
)
_DATE_PATTERNS = re.compile(r"\b(date|thaw.?date)\b", re.IGNORECASE)
_BOOL_PATTERNS = re.compile(r"\b(producer)\b", re.IGNORECASE)

# Section heading → JSON property key (camelCase) + array/object choice
SECTION_META = {
    "3.1": {"key": "experiment",          "array": False, "title": "Experiment Description"},
    "3.2": {"key": "cellLine",            "array": False, "title": "Cell Line Information"},
    "3.3": {"key": "cultureConditions",   "array": False, "title": "Culture Conditions"},
    "3.4": {"key": "processParameters",   "array": False, "title": "Process Parameters"},
    "3.5": {"key": "sampling",            "array": True,  "title": "Sampling & Time Course"},
    "3.6": {"key": "analyticalMethods",   "array": True,  "title": "Analytical Methods"},
    "3.7": {"key": "product",             "array": False, "title": "Product Information"},
}

# Known enum values for specific fields
ENUM_OVERRIDES = {
    "processType":         ["Batch", "FedBatch", "Perfusion", "Continuous", "Other"],
    "agitationType":       ["Orbital", "Pitched-blade", "Rushton", "Marine", "Other"],
    "culturePhase":        ["EarlyExponential", "MidExponential", "LateExponential",
                            "Stationary", "Decline", "Other"],
    "cellularCompartment": ["Cell", "Extracellular Region", "Nuclear", "Mitochondrial", "Other"],
    "analysisType":        ["Transcriptomics", "Metabolomics", "Glycosylation", "Proteomics",
                            "CellViability", "Titer", "Other"],
    "normalizationMethod": ["TPM", "CPM", "VST", "RPKM", "FPKM", "None", "Other"],
}

# Regex patterns for Ensembl and UniProt IDs
ID_PATTERNS = {
    "ensemblGeneID": "^ENS[A-Z]*G\\d+$",
    "uniProtID":     "^[A-Z][0-9][A-Z0-9]{3}[0-9]$",
    "publicationDOI": "^10\\.\\d{4,}(\\.\\d+)*/.*$",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def to_camel(name: str) -> str:
    """Convert MIAYBE item name to lowerCamelCase property key."""
    # Strip leading/trailing whitespace and bold markers
    name = name.strip().strip("*").strip()
    # Split on spaces, underscores, or hyphens
    parts = re.split(r"[\s_\-]+", name)
    return parts[0][0].lower() + parts[0][1:] + "".join(p.capitalize() for p in parts[1:])


def parse_table_rows(lines: list[str]) -> list[list[str]]:
    """Parse a Markdown pipe table into a list of row cell lists, skipping separator rows."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            break  # end of table
        # Skip separator row (e.g. |---|---|)
        if re.fullmatch(r"[\|\s\-:]+", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows


def infer_json_type(field_key: str, definition: str, unit: str | None) -> dict:
    """Return a JSON Schema type fragment for the field."""
    if _BOOL_PATTERNS.search(field_key):
        return {"type": "boolean"}
    if _DATE_PATTERNS.search(field_key):
        return {"type": "string", "format": "date"}
    if _NUMERIC_PATTERNS.search(field_key) or (unit and unit not in ("—", "-", "")):
        schema = {"type": "number", "minimum": 0}
        if "percentage" in field_key.lower() or "%" in (unit or ""):
            schema["maximum"] = 100
        if "ph" == field_key.lower():
            schema.update({"minimum": 6.0, "maximum": 8.0})
        if "temperature" in field_key.lower():
            schema.update({"minimum": 25, "maximum": 42})
        return schema
    if field_key in ENUM_OVERRIDES:
        return {"type": "string", "enum": ENUM_OVERRIDES[field_key]}
    if field_key in ID_PATTERNS:
        return {"type": "string", "pattern": ID_PATTERNS[field_key]}
    return {"type": "string"}


def build_property(item_id: str, raw_name: str, status: str,
                   definition: str, unit: str | None, cq: str | None) -> tuple[str, dict]:
    """Build a (property_key, property_schema) pair."""
    base_key = to_camel(raw_name)
    # Append unit suffix for numeric fields to avoid collisions
    if unit and unit not in ("—", "-", "", "—"):
        safe_unit = re.sub(r"[^a-zA-Z0-9]", "", unit)
        prop_key = f"{base_key}_{safe_unit}" if safe_unit else base_key
    else:
        prop_key = base_key

    schema = infer_json_type(prop_key, definition, unit)

    miaybe_meta = {"id": item_id, "status": status}
    if unit and unit not in ("—", "-", ""):
        miaybe_meta["unit"] = unit
    if cq and cq not in ("—", "-", ""):
        miaybe_meta["cqMapping"] = [c.strip() for c in cq.split(",") if c.strip() and c.strip() != "—"]

    title = raw_name.strip("*").strip()
    if unit and unit not in ("—", "-", ""):
        title += f" ({unit})"

    schema["title"] = title
    schema["description"] = f"[{item_id}, {status}] {definition.strip('.')}"
    schema["miaybe"] = miaybe_meta

    return prop_key, schema


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

def parse_miaybe_md(md_text: str) -> dict:
    """Parse a MIAYBE markdown file and return a JSON Schema dict."""

    lines = md_text.splitlines()

    # -- Extract version and date from the header --
    version = "unknown"
    spec_date = "unknown"
    for line in lines[:10]:
        m = re.search(r"Version\s+([\d\.]+[^\s]*)", line, re.IGNORECASE)
        if m:
            version = m.group(1).strip("()")
        m = re.search(r"Date:\s*(\S+)", line, re.IGNORECASE)
        if m:
            spec_date = m.group(1)

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"https://github.com/uga-repos/mcbo/schemas/miaybe_{version.replace(' ', '_')}.json",
        "title": f"MIAYBE {version} Dashboard Schema",
        "description": (
            f"JSON Schema for a data entry dashboard compliant with MIAYBE {version} "
            f"(Minimum Information About Your Bioprocessing Experiment). "
            f"Generated from specification dated {spec_date}. "
            "Fields tagged with MIAYBE status: R=required, M=recommended, O=optional."
        ),
        "type": "object",
        "required": [],
        "properties": {},
    }

    # -- Walk sections 3.1–3.7 --
    current_section = None
    i = 0
    section_schemas: dict[str, dict] = {}

    while i < len(lines):
        line = lines[i]

        # Detect "### 3.x" headings
        m = re.match(r"^#{2,3}\s+(3\.[1-7])\b", line)
        if m:
            current_section = m.group(1)
            i += 1
            continue

        # Detect table header rows inside a recognised section
        # Only process checklist tables that have both "ID" and "Item" columns
        if current_section and line.startswith("|") and "Item" in line and "ID" in line:
            # Determine whether this table has a "Unit" column
            header_cells = [c.strip() for c in line.strip("|").split("|")]
            if "ID" not in header_cells or "Item" not in header_cells or "Status" not in header_cells:
                i += 1
                continue
            has_unit = "Unit" in header_cells
            unit_col = header_cells.index("Unit") if has_unit else None
            # Standard columns: ID, Item, Status, Definition, [Unit,] Example, CQ Mapping
            col_id     = header_cells.index("ID")
            col_item   = header_cells.index("Item")
            col_status = header_cells.index("Status")
            col_def    = header_cells.index("Definition")
            col_cq     = header_cells.index("CQ Mapping") if "CQ Mapping" in header_cells else None

            # Collect subsequent rows
            table_lines = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1

            rows = parse_table_rows(table_lines)

            meta = SECTION_META.get(current_section)
            if not meta:
                i = j
                continue

            sec_key = meta["key"]
            if sec_key not in section_schemas:
                section_schemas[sec_key] = {
                    "title": meta["title"],
                    "description": f"Section {current_section}",
                    "type": "object",
                    "required": [],
                    "properties": {},
                }

            for row in rows:
                if len(row) < 4:
                    continue
                item_id = row[col_id].strip()
                raw_name = row[col_item].strip().strip("**")
                status = row[col_status].strip()
                definition = row[col_def].strip()
                unit = row[unit_col].strip() if unit_col is not None and unit_col < len(row) else None
                cq = row[col_cq].strip() if col_cq is not None and col_cq < len(row) else None

                prop_key, prop_schema = build_property(item_id, raw_name, status,
                                                       definition, unit, cq)
                section_schemas[sec_key]["properties"][prop_key] = prop_schema
                if status == "R":
                    section_schemas[sec_key]["required"].append(prop_key)

            if not section_schemas[sec_key]["required"]:
                del section_schemas[sec_key]["required"]

            i = j
            continue

        i += 1

    # -- Assemble top-level schema --
    for num, meta in SECTION_META.items():
        sec_key = meta["key"]
        if sec_key not in section_schemas:
            continue

        sec_schema = section_schemas[sec_key]

        if meta["array"]:
            # Wrap in array
            top_schema = {
                "title": meta["title"],
                "description": sec_schema["description"],
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "object",
                    "required": sec_schema.get("required", []),
                    "properties": sec_schema["properties"],
                },
            }
        else:
            top_schema = sec_schema

        schema["properties"][sec_key] = top_schema
        schema["required"].append(sec_key)

    return schema


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Convert a MIAYBE Markdown spec into a JSON Schema."
    )
    parser.add_argument("input", help="Path to MIAYBE Markdown file (e.g. MIAYBE.md)")
    parser.add_argument(
        "-o", "--output",
        help="Output JSON Schema file path (default: stdout)",
        default=None,
    )
    parser.add_argument(
        "--indent", type=int, default=2,
        help="JSON indentation level (default: 2)",
    )
    args = parser.parse_args()

    md_path = Path(args.input)
    if not md_path.exists():
        print(f"ERROR: File not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    md_text = md_path.read_text(encoding="utf-8")
    schema = parse_miaybe_md(md_text)
    json_text = json.dumps(schema, indent=args.indent, ensure_ascii=False)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(json_text, encoding="utf-8")
        print(f"Schema written to: {out_path}")
    else:
        print(json_text)


if __name__ == "__main__":
    main()
