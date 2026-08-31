import React, { useState, useEffect } from 'react';
import { getHealthStatus, getDetailedHealth } from '../api/api';
import StatusBadge from '../components/StatusBadge';

export default function HomePage() {
  const [basicHealth, setBasicHealth] = useState(null);
  const [detailedHealth, setDetailedHealth] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const checkConnection = async () => {
    setLoading(true);
    setError(null);

    try {
      // Fetch basic health from GET /api/health
      const basic = await getHealthStatus();
      setBasicHealth(basic);

      // Attempt detailed health from GET /api/v1/health
      try {
        const detailed = await getDetailedHealth();
        setDetailedHealth(detailed);
      } catch (detErr) {
        console.warn('Detailed health check failed:', detErr);
      }
    } catch (err) {
      console.error('API connection failure:', err);
      setError(err.message || 'Unable to connect to API');
      setBasicHealth(null);
      setDetailedHealth(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkConnection();
  }, []);

  return (
    <div className="home-page">
      <section className="hero-banner">
        <h1>Photo Group Portal</h1>
        <p className="hero-subtitle">
          Event Photography Management & Face-Matched Gallery Portal
        </p>
      </section>

      <div className="card status-panel">
        <div className="panel-header">
          <h2>Backend Connection Status</h2>
          <button 
            className="btn-refresh" 
            onClick={checkConnection}
            disabled={loading}
          >
            {loading ? 'Checking...' : '🔄 Refresh Connection'}
          </button>
        </div>

        {loading && (
          <div className="state-container loading">
            <div className="spinner"></div>
            <span>Testing connection to FastAPI backend...</span>
          </div>
        )}

        {!loading && error && (
          <div className="state-container disconnected">
            <div className="status-indicator-box error">
              <span className="indicator-icon">🔌</span>
              <div className="indicator-text">
                <h3>Backend Status: Disconnected</h3>
                <p>Unable to connect to API ({error})</p>
                <small>Ensure FastAPI server is running on port 8000.</small>
              </div>
            </div>
          </div>
        )}

        {!loading && basicHealth && (
          <div className="state-container connected">
            <div className="status-indicator-box success">
              <span className="indicator-icon">✅</span>
              <div className="indicator-text">
                <h3>Backend Status: Connected</h3>
                <p>API Status: {basicHealth.status.toUpperCase()}</p>
                <small>Service: {basicHealth.service}</small>
              </div>
            </div>

            <div className="badges-row">
              <StatusBadge status="Connected" label="Backend" />
              <StatusBadge status={basicHealth.status} label="API Status" />
              {detailedHealth && (
                <StatusBadge status={detailedHealth.database.status} label="Database" />
              )}
            </div>

            {detailedHealth && (
              <div className="metrics-grid">
                <div className="metric-card">
                  <span className="metric-label">App Name</span>
                  <span className="metric-value">{detailedHealth.app_name}</span>
                </div>
                <div className="metric-card">
                  <span className="metric-label">Environment</span>
                  <span className="metric-value">{detailedHealth.environment}</span>
                </div>
                <div className="metric-card">
                  <span className="metric-label">Version</span>
                  <span className="metric-value">{detailedHealth.version}</span>
                </div>
                <div className="metric-card">
                  <span className="metric-label">DB Dialect</span>
                  <span className="metric-value code">{detailedHealth.database.dialect}</span>
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      <section className="features-overview">
        <div className="feature-card">
          <h3>⚡ FastAPI Connection Baseline</h3>
          <p>Structured Python API service mounted on <code>/api</code> with health check contracts.</p>
        </div>
        <div className="feature-card">
          <h3>📦 Modular API Service</h3>
          <p>Encapsulated client module in <code>src/api/api.js</code> with environment-based <code>VITE_API_URL</code> configuration.</p>
        </div>
        <div className="feature-card">
          <h3>🛡️ Robust Error Isolation</h3>
          <p>Graceful handling of network timeouts, backend offline states, and non-2xx API errors.</p>
        </div>
      </section>
    </div>
  );
}
