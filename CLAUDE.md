# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MIAYBE (Minimum Information About Your Bioprocessing Experiment) is a metadata standard for describing mammalian cell culture bioprocessing experiments. The repository contains:

1. **`MIAYBE.md`** — The specification document (v1.3 draft) defining 71 metadata fields across 7 categories, aligned with the MCBO (Mammalian Cell Bioprocessing Ontology).
2. **`miaybe_md_to_schema.py`** — A Python CLI tool that parses `MIAYBE.md` and generates a JSON Schema.
3. **`miaybe_schema_generated.json`** — The generated JSON Schema output (committed artifact, regenerated from `MIAYBE.md`).

## Commands

### Generate the JSON Schema

```bash
# Output to stdout
python miaybe_md_to_schema.py MIAYBE.md

# Write to file
python miaybe_md_to_schema.py MIAYBE.md -o miaybe_schema_generated.json

# Custom indentation
python miaybe_md_to_schema.py MIAYBE.md -o miaybe_schema_generated.json --indent 4
```

The script requires only Python stdlib (no `pip install` needed).

## Architecture: Spec → Schema Pipeline

The parser (`miaybe_md_to_schema.py`) walks `MIAYBE.md` looking for `### 3.x` section headings and then parses the Markdown pipe tables beneath them. It uses column headers (`ID`, `Item`, `Status`, `Definition`, `Unit`, `CQ Mapping`) to extract field metadata.

**Section mapping** (defined in `SECTION_META`):

| Section | JSON key | Schema type |
|---------|----------|-------------|
| 3.1 Experiment Description | `experiment` | object |
| 3.2 Cell Line Information | `cellLine` | object |
| 3.3 Culture Conditions | `cultureConditions` | object |
| 3.4 Process Parameters | `processParameters` | object |
| 3.5 Sampling & Time Course | `sampling` | **array** |
| 3.6 Analytical Methods | `analyticalMethods` | **array** |
| 3.7 Product Information | `product` | object |

**Type inference** (`infer_json_type`): field names are matched against regex patterns to assign `number`, `boolean`, `string/date`, or plain `string`. Specific fields get `enum` constraints (e.g. `processType`, `culturePhase`) or regex `pattern` constraints (e.g. `ensemblGeneID`, `uniProtID`).

**Field status**: `R` (Required) fields become JSON Schema `required` entries; `M` (Recommended) and `O` (Optional) fields are present but not required.

**Property keys**: item names are converted to lowerCamelCase via `to_camel()`. Numeric fields with units get a unit suffix appended (e.g. `agitationSpeed_rpm`).

## Key Design Decisions

- `miaybe_schema_generated.json` is a derived artifact that should be regenerated whenever `MIAYBE.md` changes.
- The spec document is the source of truth; the Python script is a read-only parser of that document.
- The `ENUM_OVERRIDES` and `ID_PATTERNS` dicts in the script are the only places where schema constraints are added beyond what the Markdown tables contain.
- Emacs backup files (`*.py~`) are not gitignored by the current `.gitignore` — they appear in the repo as `miaybe_md_to_schema.py~`.
