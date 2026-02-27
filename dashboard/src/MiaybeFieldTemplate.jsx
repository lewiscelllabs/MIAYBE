import React from 'react';

const STATUS_META = {
  R: { label: 'Required',    className: 'badge-R' },
  M: { label: 'Recommended', className: 'badge-M' },
  O: { label: 'Optional',    className: 'badge-O' },
};

/**
 * Custom FieldTemplate that surfaces MIAYBE metadata (field ID and R/M/O status)
 * on every form field label via a small colour-coded badge.
 *
 * The `miaybe` object on each schema property carries:
 *   { id: "E1", status: "R", unit?: "°C", cqMapping?: ["CQ1"] }
 */
export default function MiaybeFieldTemplate({
  id,
  label,
  description,
  required,
  errors,
  children,
  schema,
  hidden,
  displayLabel,
}) {
  if (hidden) return <div>{children}</div>;

  const { status, id: miaybeId, unit } = schema?.miaybe ?? {};
  const statusMeta = STATUS_META[status];

  return (
    <div className={`field-wrap ${status ? `field-${status}` : ''}`}>
      {displayLabel && label && (
        <label htmlFor={id} className="field-label">
          <span className="label-text">{label}</span>
          {required && <span className="required-star" aria-hidden="true">*</span>}
          {miaybeId && (
            <code className="field-id" title={`MIAYBE field ${miaybeId}`}>
              {miaybeId}
            </code>
          )}
          {statusMeta && (
            <span
              className={`status-badge ${statusMeta.className}`}
              title={statusMeta.label}
            >
              {status}
            </span>
          )}
        </label>
      )}

      {description && (
        <p className="field-description">{description}</p>
      )}

      <div className="field-widget">{children}</div>

      {errors && <div className="field-errors">{errors}</div>}
    </div>
  );
}
