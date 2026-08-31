import React from 'react';

export default function StatusBadge({ status, label }) {
  const isOk = status === 'ok' || status === 'healthy' || status === 'Connected';
  const isWarning = status === 'degraded' || status?.includes('fallback');
  
  let badgeClass = 'badge-danger';
  if (isOk) badgeClass = 'badge-success';
  else if (isWarning) badgeClass = 'badge-warning';

  return (
    <span className={`status-badge ${badgeClass}`}>
      ● {label}: {status}
    </span>
  );
}
