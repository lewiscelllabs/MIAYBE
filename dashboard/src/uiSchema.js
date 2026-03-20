/**
 * RJSF uiSchema for the MIAYBE dashboard.
 *
 * Controls widget types, placeholder text, and display options for each
 * field in the generated schema.  Keys mirror the camelCase property names
 * produced by miaybe_md_to_schema.py.
 *
 * RJSF docs: https://rjsf-team.github.io/react-jsonschema-form/docs/api-reference/uiSchema
 */
export const uiSchema = {
  // Hide the default RJSF submit button — App.jsx renders its own.
  'ui:submitButtonOptions': { norender: true },

  // ── 3.1 Experiment Description ───────────────────────────────────────────
  experiment: {
    experimentDate: {
      'ui:widget': 'date',
    },
    experimentObjective: {
      'ui:widget': 'textarea',
      'ui:options': { rows: 3 },
      'ui:placeholder': 'e.g. Effect of temperature shift on glycosylation',
    },
    publicationDOI: {
      'ui:placeholder': '10.1234/journal.article',
    },
  },

  // ── 3.2 Cell Line Information ─────────────────────────────────────────────
  cellLine: {
    thawDate: {
      'ui:widget': 'date',
    },
    passageNumber: {
      'ui:placeholder': 'e.g. P15',
    },
    geneticModification: {
      'ui:placeholder': 'e.g. hSt6Gal1 overexpression',
    },
    selectionMarker: {
      'ui:placeholder': 'e.g. GS-/-, DHFR, Puromycin',
    },
  },

  // ── 3.3 Culture Conditions ────────────────────────────────────────────────
  cultureConditions: {
    mediaSupplements: {
      'ui:widget': 'textarea',
      'ui:options': { rows: 2 },
      'ui:placeholder': 'e.g. 8 mM L-Glutamine, Anti-clumping agent',
    },
    vesselType: {
      'ui:placeholder': 'e.g. 125 mL Erlenmeyer, 2 L STR',
    },
  },

  // ── 3.4 Process Parameters ────────────────────────────────────────────────
  processParameters: {
    cultureDuration: {
      'ui:placeholder': 'e.g. 14 days',
    },
    harvestCriteria: {
      'ui:placeholder': 'e.g. Viability <70% or Day 14',
    },
    feedSchedule: {
      'ui:placeholder': 'e.g. Days 3, 5, 7, 9, 11',
    },
    feedComposition: {
      'ui:placeholder': 'e.g. Cell Boost 7a + 7b',
    },
    temperatureShift: {
      'ui:placeholder': 'e.g. 37→32°C on Day 4',
    },
    pHControl: {
      'ui:placeholder': 'e.g. CO₂ / base (NaHCO₃) addition',
    },
    doControl: {
      'ui:placeholder': 'e.g. O₂ sparging',
    },
    bleedStrategy: {
      'ui:placeholder': 'e.g. 0.5 VVD continuous bleed',
    },
  },

  // ── 3.5 Sampling & Time Course (array) ───────────────────────────────────
  sampling: {
    items: {
      'ui:title': 'Sample',
      sampleType: {
        'ui:placeholder': 'e.g. Cell pellet, Supernatant, Whole culture',
      },
      sampleBuffer: {
        'ui:placeholder': 'e.g. 20 mM Tris, 0.1 M NaCl, pH 7.5',
      },
      storageConditions: {
        'ui:placeholder': 'e.g. -80°C',
      },
    },
  },

  // ── 3.6 Analytical Methods (array) ───────────────────────────────────────
  analyticalMethods: {
    items: {
      'ui:title': 'Analytical Method',
      metabolitePanel: {
        'ui:placeholder': 'e.g. Glc, Lac, Gln, NH₄⁺ via BioProfile 400',
      },
      sequencingDepth: {
        'ui:placeholder': 'e.g. 20M reads/sample',
      },
      platform: {
        'ui:placeholder': 'e.g. Illumina NovaSeq 6000',
      },
      protocolReference: {
        'ui:placeholder': 'e.g. SOP-MET-001 or PMID:12345678',
      },
      dataProcessingPipeline: {
        'ui:placeholder': 'e.g. STAR 2.7.9a → DESeq2 1.34',
      },
    },
  },

  // ── 3.7 Product Information ───────────────────────────────────────────────
  product: {
    productType: {
      'ui:placeholder': 'e.g. mAb IgG1, Fusion protein',
    },
    qualityType: {
      'ui:placeholder': 'e.g. Glycosylation, Aggregation',
    },
    ensemblGeneID: {
      'ui:placeholder': 'ENSG00000197249',
    },
    uniProtID: {
      'ui:placeholder': 'P01009',
    },
  },
};
