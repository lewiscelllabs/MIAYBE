# MIAYBE: Minimum Information About Your Bioprocessing Experiment

**Version 1.3 (Draft)**
**Date: 2026-02-10**

## Abstract

MIAYBE (Minimum Information About Your Bioprocessing Experiment) defines the minimum information required to unambiguously describe a biologics manufacturing experiment and enable meaningful data integration, meta-analysis, and reproducibility assessment. This guideline applies to cell culture-based production of recombinant proteins, monoclonal antibodies, and other biologics, with emphasis on mammalian cell systems (particularly CHO cells).

MIAYBE follows the precedent established by other minimum information standards including MIAME (microarray), MIQE (qPCR), MIAPE (proteomics), and MIAPPE (plant phenotyping). It provides a structured framework for reporting bioprocessing experimental conditions, enabling cross-study comparisons and supporting ontology-driven knowledge graphs such as MCBO (Mammalian Cell Bioprocessing Ontology).

---

## 1. Introduction

### 1.1 Background

Biologics manufacturing using mammalian cell culture has become the dominant platform for producing therapeutic proteins, with the global biopharmaceuticals market exceeding $400 billion annually. Despite the maturity of the field, significant challenges remain in:

- **Reproducibility**: Studies often lack sufficient detail to replicate culture conditions
- **Data integration**: Heterogeneous reporting makes cross-study meta-analysis difficult
- **Knowledge transfer**: Lessons learned in one context cannot easily be applied to others
- **Process optimization**: Machine learning approaches require standardized, structured data

The proliferation of high-throughput omics technologies (transcriptomics, metabolomics, glycomics) in bioprocessing research has created an urgent need for standardized metadata reporting. Without adequate experimental context, expression profiles and metabolite measurements cannot be meaningfully interpreted or compared.

### 1.2 Scope

MIAYBE applies to experiments involving:

- **Cell systems**: Mammalian cell lines (CHO, HEK293, NS0, hybridomas) and other eukaryotic expression hosts
- **Products**: Recombinant proteins, monoclonal antibodies (mAb), bispecific antibodies, fusion proteins, biosimilars
- **Process types**: Batch, fed-batch, perfusion, and continuous culture processes
- **Scales**: From microplate (mL) through shake flask (L) to production bioreactor (kL)
- **Analytical outputs**: Metabolomics, transcriptomics, proteomics, glycomics, cell characterization

MIAYBE does **not** cover:
- Microbial fermentation (see MIRRI guidelines)
- Downstream processing (purification, formulation)
- Clinical trial data (see ICH guidelines)
- Raw sequencing data format (see MINSEQE)

### 1.3 Relationship to Other Standards

| Standard | Scope | MIAYBE Relationship |
|----------|-------|---------------------|
| MIAME | Microarray experiments | Expression data context |
| MINSEQE | Sequencing experiments | RNA-seq/NGS context |
| MIQE | qPCR experiments | Validation assays |
| MIAPE | Proteomics | Product characterization |
| MIAPPE | Plant phenotyping | Structural model reference |
| ISA-TAB | Investigation-Study-Assay | Data exchange format |
| MCBO | Bioprocessing ontology | Semantic framework |

---

## 2. MIAYBE Checklist Overview

MIAYBE organizes required information into seven categories, with items classified as:

- **REQUIRED (R)**: Must be reported for the experiment to be interpretable
- **RECOMMENDED (M)**: Should be reported when available; critical for reproducibility
- **OPTIONAL (O)**: Useful for comprehensive documentation but not essential

### Summary Table

| Category | Required | Recommended | Optional | Total |
|----------|----------|-------------|----------|-------|
| 1. Experiment Description | 4 | 2 | 2 | 8 |
| 2. Cell Line Information | 4 | 4 | 4 | 12 |
| 3. Culture Conditions | 5 | 6 | 4 | 15 |
| 4. Process Parameters | 3 | 4 | 3 | 10 |
| 5. Sampling & Time Course | 4 | 4 | 3 | 11 |
| 6. Analytical Methods | 3 | 3 | 2 | 8 |
| 7. Product Information | 2 | 3 | 2 | 7 |
| **Total** | **25** | **26** | **20** | **71** |

---

## 3. Detailed Requirements

### 3.1 Experiment Description

Information identifying and contextualizing the experiment.

| ID | Item | Status | Definition | Example | CQ Mapping |
|----|------|--------|------------|---------|------------|
| E1 | **ExperimentID** | R | Unique identifier for the experiment | EXPT586, CBD10 | — |
| E2 | **StudyID** | R | Identifier grouping related experiments | study_cho_glyco | All CQs |
| E3 | **ExperimentDate** | R | Start date of the experiment | 2020-02-25 | — |
| E4 | **ExperimentObjective** | R | Primary scientific question | "Effect of temperature on glycosylation" | — |
| E5 | **InvestigatorName** | M | Lead researcher/operator | Sanne Schoffelen | — |
| E6 | **InstitutionName** | M | Performing institution | University of Georgia | — |
| E7 | **FundingSource** | O | Grant or funding information | NIH R01-GM123456 | — |
| E8 | **PublicationDOI** | O | Associated publication DOI | 10.1038/s41587-020-0123-4 | — |

### 3.2 Cell Line Information

Complete characterization of the biological material.

| ID | Item | Status | Definition | Example | CQ Mapping |
|----|------|--------|------------|---------|------------|
| C1 | **CellLine** | R | Cell line name/designation | CHO-S, CHO-K1, HEK293 | CQ1-8 |
| C2 | **Host** | R | Base organism | CHO (Cricetulus griseus) | — |
| C3 | **CellLineSource** | R | Origin/vendor of cell line | ATCC, Thermo Fisher, In-house | — |
| C4 | **CloneID** | R | Specific clone identifier | CHO_S_47_2_6(37-1#7-C1) | CQ4, CQ8 |
| C5 | **ParentCellLine** | M | Parental line if derived | CHO-K1 (for CHO-S derivative) | — |
| C6 | **GeneticModification** | M | Transgenes or knockouts | hSt6Gal1 overexpression | — |
| C7 | **SelectionMarker** | M | Selection system used | GS-/-, DHFR, Puromycin | — |
| C8 | **PassageNumber** | M | Passage at experiment start | P15, P20-25 | — |
| C9 | **Producer** | O | Whether line is a producer | TRUE (produces recombinant product) | CQ2 |
| C10 | **Stability** | O | Expression stability status | Stable >50 generations | — |
| C11 | **CellBankID** | O | Reference to banked cells | MCB-2020-001 | — |
| C12 | **ThawDate** | O | Date cells were thawed from bank | 2019-11-29 | — |

### 3.3 Culture Conditions

Physical and chemical environment parameters.

| ID | Item | Status | Definition | Unit | Example | CQ Mapping |
|----|------|--------|------------|------|---------|------------|
| CC1 | **Temperature** | R | Culture temperature | °C | 37, 32.5 | CQ1 |
| CC2 | **pH** | R | Culture pH (setpoint or measured) | — | 7.0, 6.8-7.2 | CQ1 |
| CC3 | **DissolvedOxygen** | R | DO level | % air sat. | 40, 30-50 | CQ1 |
| CC4 | **BaseMedium** | R | Growth medium | — | CD CHO, EX-CELL | — |
| CC5 | **MediaSupplements** | R | Additives beyond base | — | 8 mM Gln, Anti-clumping | — |
| CC6 | **GlutamineConcentration** | M | Initial Gln concentration | mM | 4.0, 8.0 | CQ3 |
| CC7 | **GlucoseConcentration** | M | Initial glucose | g/L | 6.0 | — |
| CC8 | **OsmolalitySetpoint** | M | Target osmolality | mOsm/kg | 300-330 | — |
| CC9 | **CO2Percentage** | M | Incubator CO2 | % | 5, 8 | — |
| CC10 | **AgitationSpeed** | M | Stirrer/shaker speed | rpm | 120, 150 | — |
| CC11 | **AgitationType** | M | Mixing mode | — | Orbital, Pitched-blade | — |
| CC12 | **InoculationDensity** | O | Seeding cell density | cells/mL | 3×10⁵ | — |
| CC13 | **CultureVolume** | O | Working volume | mL | 30, 1000 | — |
| CC14 | **VesselType** | O | Bioreactor/flask type | — | Erlenmeyer 125mL, 2L STR | — |
| CC15 | **ShakerDiameter** | O | Orbital shaking throw | mm | 25 | — |

### 3.4 Process Parameters

Operational mode and feeding strategy.

| ID | Item | Status | Definition | Example | CQ Mapping |
|----|------|--------|------------|---------|------------|
| P1 | **ProcessType** | R | Culture mode | Batch, FedBatch, Perfusion | CQ5 |
| P2 | **CultureDuration** | R | Total culture length | 14 days, 72 hours | — |
| P3 | **HarvestCriteria** | R | Termination trigger | Viability <70%, Day 14 | — |
| P4 | **FeedStrategy** | M | Feeding protocol | Daily bolus 3% v/v, Continuous | — |
| P5 | **FeedComposition** | M | Feed medium type | Cell Boost 7a/7b | — |
| P6 | **FeedSchedule** | M | Timing of feeds | Days 3,5,7,9 | — |
| P7 | **TemperatureShift** | M | Temperature reduction | 37→32°C on Day 4 | — |
| P8 | **pHControl** | O | pH control method | CO₂/base addition | — |
| P9 | **DOControl** | O | DO control method | O₂ sparging | — |
| P10 | **BleedStrategy** | O | Perfusion bleed rate | 0.5 VVD | — |

### 3.5 Sampling & Time Course

Sample collection and state at collection.

| ID | Item | Status | Definition | Unit | Example | CQ Mapping |
|----|------|--------|------------|------|---------|------------|
| S1 | **SampleAccession** | R | Unique sample identifier | — | CC207_EnM, ERS4805133 | All CQs |
| S2 | **CollectionTimepoint** | R | Time of sample collection | hours | 0, 48, 72 | CQ3 |
| S3 | **ViableCellDensity** | R | VCD at collection | cells/mL | 8.5×10⁶ | CQ3 |
| S4 | **ViabilityPercentage** | R | % viability at collection | % | 95, 87 | CQ7 |
| S5 | **CulturePhase** | M | Growth phase at sampling | — | EarlyExp, LateExp, Stationary | CQ4, CQ6 |
| S6 | **SampleType** | M | Type of sample collected | — | Cell pellet, Supernatant, Whole culture | — |
| S7 | **SampleVolume** | M | Volume collected | mL | 1.0 | — |
| S8 | **CellularCompartment** | M | Cellular origin of the sample | — | Extracellular Region, Cell (intracellular) | — |
| S9 | **SampleBuffer** | O | Buffer/matrix for purified samples | — | 20 mM Tris, 0.1M NaCl, pH 7.5 | — |
| S10 | **StorageConditions** | O | Sample preservation | — | -80°C, Liquid N₂ | — |
| S11 | **ProcessingDelay** | O | Time from collection to processing | min | <30 | — |

### 3.6 Analytical Methods

Assays and measurements performed.

| ID | Item | Status | Definition | Example | CQ Mapping |
|----|------|--------|------------|---------|------------|
| A1 | **AnalysisType** | R | Category of analysis | Transcriptomics, Metabolomics, Glycosylation | — |
| A2 | **Platform** | R | Instrument/technology | Illumina NovaSeq, SCIEX TripleTOF | — |
| A3 | **ProtocolReference** | R | SOP or publication reference | SOP-MET-001, PMID:12345678 | — |
| A4 | **MetabolitePanel** | M | For metabolomics: analytes measured | BioProfile 400: Glc, Lac, Gln, NH₄⁺ | — |
| A5 | **LibraryStrategy** | M | For RNA-seq: library prep method | rRNA depletion, PolyA selection | — |
| A6 | **SequencingDepth** | M | For RNA-seq: target depth | 20M reads/sample | — |
| A7 | **DataProcessingPipeline** | O | Analysis software/version | STAR 2.7.9a, Salmon 1.5.0 | — |
| A8 | **NormalizationMethod** | O | Data normalization approach | TPM, CPM, VST | — |

### 3.7 Product Information

Details about the recombinant product (for producer cell lines).

| ID | Item | Status | Definition | Example | CQ Mapping |
|----|------|--------|------------|---------|------------|
| PR1 | **ProductType** | R | Class of product | mAb, IgG1, Fusion protein, AMBP | CQ2, CQ8 |
| PR2 | **ProductName** | R | Product identifier | Rituximab, hAAT | — |
| PR3 | **TiterValue** | M | Product concentration | mg/L | 1500 | CQ8 |
| PR4 | **TiterMethod** | M | Quantification assay | ELISA, Protein A HPLC | — |
| PR5 | **QualityType** | M | Quality attribute assessed | Glycosylation, Aggregation | CQ8 |
| PR6 | **EnsemblGeneID** | O | For protein products: gene ID | ENSG00000197249 | — |
| PR7 | **UniProtID** | O | Protein database reference | P01009 | — |

---

## 4. Mapping to MCBO Ontology

MIAYBE items map to the MCBO (Mammalian Cell Bioprocessing Ontology) data dictionary as follows:

| MIAYBE Item | MCBO Column | Notes |
|-------------|-------------|-------|
| ExperimentID | StudyID | Grouped by study |
| CellLine | CellLine | Direct mapping |
| CloneID | CloneID | Direct mapping |
| Host | Host | "CHO" for CHO lines |
| GeneticModification | GeneticModification | Plasmid/transgene info |
| SelectionMarker | SelectionMarker | GS, DHFR, etc. |
| Temperature | Temperature | Decimal °C |
| pH | pH | Decimal |
| DissolvedOxygen | DissolvedOxygen | % air saturation |
| GlutamineConcentration | GlutamineConcentration | mM |
| ProcessType | ProcessType | Batch/FedBatch/Perfusion |
| CollectionTimepoint | CollectionDay | Converted to days |
| CulturePhase | CulturePhase | EarlyExp/MidExp/LateExp/Stationary |
| ViableCellDensity | ViableCellDensity | cells/mL |
| ViabilityPercentage | ViabilityPercentage | 0-100% |
| ProductType | ProductType | Gene symbol or antibody term |
| TiterValue | TiterValue | mg/L |
| QualityType | QualityType | Glycosylation, Aggregation, etc. |
| SampleAccession | SampleAccession | Unique identifier |
| Producer | Producer | Boolean |
| CellularCompartment | CellularCompartment | "Cell" or "Extracellular Region" |
| ThawDate | ThawDate | Date cells thawed from bank |
| SampleBuffer | Buffer | For purified protein samples |

### Competency Question Coverage

MIAYBE requirements directly support the following MCBO competency questions:

| CQ | Question | MIAYBE Requirements | Data Source |
|----|----------|---------------------|-------------|
| CQ1 | What culture conditions are associated with high productivity? | CC1-3 (T, pH, DO), P1, PR3 | `titer` table (co-located conditions) |
| CQ2 | Which CHO cell lines overexpress specific genes? | C1 (CellLine), C9 (Producer), PR1 | `sample_metadata` table |
| CQ3 | What nutrients support high viability? | CC6 (Gln), CC7 (Glc), S3 (VCD) | `titer` table (co-located nutrients + VCD) |
| CQ4 | How does expression differ between clones? | C4 (CloneID), S5 (Phase) | `gene_expression_tpm` + `sample_metadata` |
| CQ5 | What genes are differentially expressed (FedBatch vs Batch)? | P1 (ProcessType) | `gene_expression_tpm` + `sample_metadata` |
| CQ6 | Which genes correlate with productivity? | S5 (Phase), PR3 (Titer) | `gene_expression_tpm` + `sample_metadata` |
| CQ7 | What genes differ by viability threshold? | S4 (Viability %) | `gene_expression_tpm` + `sample_metadata` |
| CQ8 | Which cell lines have quality profiles? | C1, C4, PR3, PR5 | `sample_metadata` table |

---

## 5. Data Format Recommendations

### 5.1 File Formats

| Data Type | Recommended Format | Alternative |
|-----------|-------------------|-------------|
| Sample metadata | CSV (UTF-8) | TSV, ISA-TAB |
| Expression matrices | CSV (samples × genes) | HDF5, Parquet |
| Metabolomics | mzML + CSV summary | mzXML |
| Glycosylation profiles | CSV | GlycoMod XML |
| Time series | CSV with timepoint column | JSON |

### 5.2 Naming Conventions

**Sample Identifiers**: Use consistent hierarchical naming:
```
{StudyID}_{CultureID}_{SampleType}_{Timepoint}
Example: CBD10_CC207_EnM_72h
```

**File Naming**:
```
{StudyID}_sample_metadata.csv
{StudyID}_expression_matrix.csv
{StudyID}_metabolomics_summary.csv
```

### 5.3 Missing Values

- Use empty cells (not "NA", "N/A", or "None") for missing numeric values
- Use "not_measured" for categorical fields that weren't assessed
- Use "not_applicable" for fields that don't apply to the sample type

---

## 6. Implementation Guidelines

### 6.1 For Researchers

1. **Plan ahead**: Design your metadata collection alongside the experiment
2. **Use templates**: Download MIAYBE-compliant spreadsheet templates
3. **Record in real-time**: Capture conditions as they occur, not retrospectively
4. **Version control**: Track changes to metadata files
5. **Archive raw data**: Preserve original instrument outputs alongside processed summaries

### 6.2 For Data Repositories

1. **Validate submissions**: Check for required fields before acceptance
2. **Provide feedback**: Alert submitters to missing recommended fields
3. **Support versioning**: Allow metadata updates post-submission
4. **Enable queries**: Index MIAYBE fields for search and filtering
5. **Link to ontologies**: Map to MCBO, CLO, OBI terms where possible

### 6.3 For Journal Publishers

1. **Require compliance**: Make MIAYBE adherence a submission requirement
2. **Provide checklists**: Include MIAYBE checklist in author guidelines
3. **Review metadata**: Train reviewers to assess metadata completeness
4. **Link data**: Require data repository accession numbers

---

## 6.4 Co-located Titer and Culture Conditions

A key data pattern in bioprocessing is **co-located measurements**: titer values recorded alongside culture conditions at the same timepoint. This enables direct correlation analysis without complex table joins.

**Example from ambr bioreactor data:**

| Measurement | Unit | Coverage | CQ Relevance |
|-------------|------|----------|--------------|
| TiterValue | ug/mL | 284 records | CQ1 (productivity) |
| ViableCellDensity | cells/mL | 250 records | CQ3 (VCD-nutrient correlation) |
| Viability | % | 250 records | CQ7 (viability thresholds) |
| Glucose | mM | 250 records | CQ3 (nutrient analysis) |
| Glutamine | mM | 249 records | CQ3 (nutrient analysis) |
| pH | - | 69 records | CQ1 (culture conditions) |
| Osmolality | mOsm/kg | 111 records | Culture optimization |

**Key correlations identified:**
- pH vs Titer: r=+0.717 (strong positive, optimal range 7.15-7.20)
- Glucose vs VCD: r=-0.742 (strong negative, nutrient depletion)
- Glutamine vs VCD: r=-0.654 (strong negative, nutrient depletion)

When reporting titer measurements, MIAYBE **recommends** including co-located culture condition values measured at the same timepoint.

---

## 6.5 Multi-Agent Query Architecture

MIAYBE-compliant datasets support automated analysis via multi-agent LLM pipelines. The reference implementation uses a 4-phase architecture:

1. **SQL Agent**: Fetches data using schema-aware queries
2. **Auto-Stats**: Deterministic pre-analysis (peak finding, correlations)
3. **Analysis Agent**: LLM interprets data with domain knowledge
4. **Critic Agent**: Validates answer completeness and accuracy

**Evidence Capture**: Each phase produces structured evidence:
- SQL queries executed (text)
- Tabular data returned (sample rows)
- Agent reasoning traces (LLM responses)
- Critic verdicts and revision requests

This architecture enables reproducible, auditable answers to MIAYBE competency questions.

---

## 7. Versioning and Governance

### 7.1 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.3-draft | 2026-02-10 | Added nb2 (Plasma proteins) dataset: 45 protein characterization samples, 292 titer records from ambr bioreactor data; notebook-specific config architecture for multi-notebook ETL |
| 1.2-draft | 2026-02-09 | Added CellularCompartment (S8), SampleBuffer (S9), ThawDate (C12) from parsed ELN data; updated MCBO mapping; updated viability data ranges for multi-notebook ID prefixing |
| 1.1-draft | 2026-02-06 | Added titer table as data source for CQ1/CQ3; updated CQ table with data sources; added multi-agent architecture reference |
| 1.0-draft | 2026-02-02 | Initial proposal |

### 7.2 Governance

MIAYBE is maintained by the MCBO Consortium. Proposed changes should be submitted as GitHub issues to the MCBO repository. Major revisions require community review and consensus.

### 7.3 Extension Mechanism

MIAYBE can be extended for specific applications:
- **MIAYBE-Gly**: Extended glycosylation metadata
- **MIAYBE-Met**: Extended metabolomics metadata
- **MIAYBE-Perf**: Extended perfusion process metadata

---

## 8. Worked Example

### 8.1 Fed-Batch CHO Culture Study

**Experiment Description**
```yaml
ExperimentID: CBD10
StudyID: study_cho_glyco
ExperimentDate: 2020-02-25
ExperimentObjective: "Characterize effect of temperature shift on glycosylation"
InvestigatorName: Sanne Schoffelen
InstitutionName: University of Georgia
```

**Cell Line Information**
```yaml
CellLine: CHO_S_47_2_6(37-1#7-C1)
Host: CHO
CellLineSource: In-house
CloneID: 37-1#7-C1
ParentCellLine: CHO-S
GeneticModification: hAAT expression, hSt6Gal1 overexpression
SelectionMarker: GS-/-
Producer: TRUE
ThawDate: 2019-11-29
```

**Culture Conditions**
```yaml
Temperature: 37 (shifted to 32 on Day 3)
pH: 7.0
DissolvedOxygen: 40
BaseMedium: CD CHO
MediaSupplements: Anti-clumping agent, 8 mM L-Glutamine
GlutamineConcentration: 8.0
AgitationSpeed: 120
AgitationType: Orbital
InoculationDensity: 3e5
CultureVolume: 30
VesselType: 125mL Erlenmeyer shake flask
ShakerDiameter: 25
```

**Process Parameters**
```yaml
ProcessType: FedBatch
CultureDuration: 14 days
HarvestCriteria: Viability <70% or Day 14
FeedStrategy: Bolus addition 3% v/v
FeedComposition: Cell Boost 7a + 7b
FeedSchedule: Days 3, 5, 7, 9, 11
TemperatureShift: 37→32°C on Day 3
```

**Sample (72h timepoint)**
```yaml
SampleAccession: CC207_EnM
CollectionTimepoint: 72
ViableCellDensity: 8.5e6
ViabilityPercentage: 95
CulturePhase: LateExponential
SampleType: Cell pellet (Endometabolome)
CellularCompartment: Cell
```

**Product Information**
```yaml
ProductType: A1AT (SERPINA1)
ProductName: Human alpha-1 antitrypsin
EnsemblGeneID: ENSG00000197249
```

---

## 9. References

### Minimum Information Standards

1. Brazma A, et al. (2001) Minimum information about a microarray experiment (MIAME). *Nature Genetics* 29:365-371. [MIAME]
2. Bustin SA, et al. (2009) The MIQE guidelines. *Clinical Chemistry* 55:611-622. [MIQE]
3. Taylor CF, et al. (2007) The minimum information about a proteomics experiment (MIAPE). *Nature Biotechnology* 25:887-893. [MIAPE]
4. Cwiek-Kupczynska H, et al. (2016) Measures for interoperability of phenotypic data: MIAPPE. *Plant Methods* 12:44. [MIAPPE]
5. Field D, et al. (2008) The minimum information about a genome sequence (MIGS). *Nature Biotechnology* 26:541-547. [MIGS/MIMS]

### Bioprocessing References

6. Li F, et al. (2010) Cell culture processes for monoclonal antibody production. *mAbs* 2:466-479.
7. Wurm FM (2004) Production of recombinant protein therapeutics in cultivated mammalian cells. *Nature Biotechnology* 22:1393-1398.
8. Kelley B (2009) Industrialization of mAb production technology. *mAbs* 1:443-452.

### Ontologies and Data Standards

9. Cell Line Ontology (CLO): https://github.com/CLO-ontology/CLO
10. Ontology for Biomedical Investigations (OBI): http://obi-ontology.org/
11. Mammalian Cell Bioprocessing Ontology (MCBO): https://github.com/uga-repos/mcbo

---

## 10. Appendix: Quick Reference Card

### Required Fields (25 items)

**Experiment**: ExperimentID, StudyID, ExperimentDate, ExperimentObjective

**Cell Line**: CellLine, Host, CellLineSource, CloneID

**Culture Conditions**: Temperature, pH, DissolvedOxygen, BaseMedium, MediaSupplements

**Process**: ProcessType, CultureDuration, HarvestCriteria

**Sampling**: SampleAccession, CollectionTimepoint, ViableCellDensity, ViabilityPercentage

**Analysis**: AnalysisType, Platform, ProtocolReference

**Product**: ProductType, ProductName

### Reporting Template

A machine-readable template is available at:
```
https://github.com/uga-repos/mcbo/templates/miabbe_template.csv
```

### Validation Tool

Validate your metadata against MIAYBE using:
```bash
mcbo-validate --schema miabbe --input my_metadata.csv
```

---

## Document Information

**Title**: MIAYBE: Minimum Information About Your Bioprocessing Experiment
**Version**: 1.3 (Draft)
**Status**: Community Review
**License**: CC-BY 4.0
**Contact**: mcbo-consortium@example.org
**Repository**: https://github.com/uga-repos/mcbo

---

---

## 11. Data Linkage: Viability and Gene Expression

### 11.1 Viability Data Source

Viability measurements are extracted from Culture Entry Excel files (NC-250 sheet) and stored in a dedicated `viability` table. All IDs carry a notebook prefix (e.g., `nb1:`) to support multi-notebook datasets (see `ADDING_DATA.md`):

| Column | Description | Coverage |
|--------|-------------|----------|
| CultureID | Notebook-prefixed culture identifier (e.g., `nb1:CC207`) | 416 cultures |
| ViabilityPct | Viability percentage | 19.2% - 96.8% |
| ViableCellDensity | Viable cells/mL | 92,700 - 6,180,000 |
| TimepointHours | Hours post-inoculation | 2h - 75h |
| BatchID | Notebook-prefixed batch identifier (e.g., `nb1:CBD10`) | nb1:CBD3 - nb1:CBD18 |

### 11.2 Linkage to Gene Expression

The viability table links to gene expression via `CultureID = SampleID`:

```sql
SELECT v.ViabilityPct, e.GeneSymbol, e.TPM
FROM viability v
JOIN gene_expression_tpm e ON v.CultureID = e.SampleID
WHERE v.ViabilityPct > 90 OR v.ViabilityPct < 50
```

**Coverage for CQ7:**
- 368 cultures have both viability AND gene expression data
- High viability (>90%): 4 cultures
- Low viability (<50%): 89 cultures
- Medium (50-90%): 275 cultures

### 11.3 Known Data Gaps

| CQ | Issue | Impact |
|----|-------|--------|
| CQ4 | Serpina1 TPM = 0.0 across all samples | Gene is not expressed; try other genes (e.g., Gapdh) |
| CQ5 | Only 1 Batch sample has gene expression (vs 367 FedBatch) | Insufficient data for differential expression |
| CQ6 | `sample_metadata.Productivity` column is sparsely populated | Limited productivity-gene correlation data |

**Note:** CQ7 is now supported via the viability table linkage.

**Recommendations for future datasets:**
- Ensure balanced representation of process types (Batch vs FedBatch)
- Verify target genes have detectable expression levels before analysis

---

*This document was developed based on analysis of real-world bioprocessing data from CHO cell culture experiments, including the Big Data Glyco Project electronic lab notebook exports, and aligned with the MCBO ontology data dictionary.*
