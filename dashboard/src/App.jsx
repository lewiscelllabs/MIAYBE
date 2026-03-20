import React, { useState } from 'react';
import Form from '@rjsf/core';
import { customizeValidator } from '@rjsf/validator-ajv8';

// Generated schema lives one level up; @schema alias is configured in vite.config.js.
// Strip $schema/$id before passing to RJSF — RJSF uses draft-07 internally and
// the draft-2020-12 $schema declaration would trigger AJV meta-schema errors.
import rawSchema from '@schema/miaybe_schema_generated.json';

import { uiSchema } from './uiSchema';
import MiaybeFieldTemplate from './MiaybeFieldTemplate';
import SectionTabsTemplate from './SectionTabsTemplate';

const { $schema, $id, title: schemaTitle, ...schema } = rawSchema;
const schemaVersion = schemaTitle?.match(/^MIAYBE\s+([^\s]+)/i)?.[1] ?? 'unknown';

// Teach AJV8 to accept the custom `miaybe` extension keyword used in the schema.
const validator = customizeValidator({
  localizer: (ajv) => {
    ajv.addKeyword('miaybe');
  },
});

export default function App() {
  const [formData, setFormData] = useState({});
  const [submitted, setSubmitted] = useState(false);

  function handleSubmit({ formData }) {
    setSubmitted(true);
    const filename = `${formData.experiment?.experimentID ?? 'miaybe'}_metadata.json`;
    const blob = new Blob([JSON.stringify(formData, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>MIAYBE Metadata Dashboard</h1>
        <p className="app-subtitle">
          Minimum Information About Your Bioprocessing Experiment — v{schemaVersion}
        </p>
        <p className="badge-legend">
          <span className="status-badge badge-R">R</span> Required &nbsp;
          <span className="status-badge badge-M">M</span> Recommended &nbsp;
          <span className="status-badge badge-O">O</span> Optional
        </p>
      </header>

      <main className="app-main">
        {submitted && (
          <div className="submit-banner">
            Metadata exported successfully. Fill in another experiment above.
          </div>
        )}

        <Form
          schema={schema}
          uiSchema={uiSchema}
          formData={formData}
          validator={validator}
          templates={{
            FieldTemplate: MiaybeFieldTemplate,
            ObjectFieldTemplate: SectionTabsTemplate,
          }}
          onChange={({ formData: fd }) => { setFormData(fd); setSubmitted(false); }}
          onSubmit={handleSubmit}
          onError={(errors) => console.error('Validation errors:', errors)}
        >
          <div className="form-actions">
            <button type="submit" className="btn-export">
              Export Metadata JSON
            </button>
          </div>
        </Form>
      </main>
    </div>
  );
}
