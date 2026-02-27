import React, { useState } from 'react';

// Human-readable tab labels keyed by the schema property name.
const SECTION_LABELS = {
  experiment:         '1. Experiment',
  cellLine:           '2. Cell Line',
  cultureConditions:  '3. Culture Conditions',
  processParameters:  '4. Process Parameters',
  sampling:           '5. Sampling',
  analyticalMethods:  '6. Analytical Methods',
  product:            '7. Product',
};

/**
 * Custom ObjectFieldTemplate for RJSF.
 *
 * - At the root level (idSchema.$id === 'root') it renders the 7 MIAYBE sections
 *   as a tabbed navigation panel.
 * - For nested objects (e.g. individual sampling items) it falls back to a plain
 *   fieldset so the tab logic doesn't recurse.
 */
export default function SectionTabsTemplate({
  title,
  description,
  properties,
  idSchema,
}) {
  const [activeTab, setActiveTab] = useState(0);

  // Nested objects: plain fieldset rendering.
  if (idSchema.$id !== 'root') {
    return (
      <fieldset className="nested-fieldset">
        {title && <legend className="nested-legend">{title}</legend>}
        {description && <p className="nested-description">{description}</p>}
        {properties.map((prop) => (
          <div key={prop.name}>{prop.content}</div>
        ))}
      </fieldset>
    );
  }

  // Root level: tabbed sections.
  return (
    <div className="section-tabs">
      <nav className="tab-nav" role="tablist">
        {properties.map((prop, idx) => (
          <button
            key={prop.name}
            role="tab"
            aria-selected={activeTab === idx}
            className={`tab-btn ${activeTab === idx ? 'tab-active' : ''}`}
            onClick={() => setActiveTab(idx)}
            type="button"
          >
            {SECTION_LABELS[prop.name] ?? prop.name}
          </button>
        ))}
      </nav>

      <div className="tab-panels">
        {properties.map((prop, idx) => (
          <div
            key={prop.name}
            role="tabpanel"
            hidden={activeTab !== idx}
            className="tab-panel"
          >
            {prop.content}
          </div>
        ))}
      </div>
    </div>
  );
}
