import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [health, setHealth] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const fetchHealth = async () => {
    setLoading(true)
    setError(null)
    try {
      // Try relative API endpoint via Vite proxy first, fallback to direct localhost:8000
      let res = await fetch('/api/v1/health').catch(() => null)
      if (!res || !res.ok) {
        res = await fetch('http://localhost:8000/api/v1/health')
      }
      
      if (!res.ok) {
        throw new Error(`Server returned HTTP status ${res.status}`)
      }
      
      const data = await res.json()
      setHealth(data)
    } catch (err) {
      console.error('Failed to fetch health status:', err)
      setError(err.message || 'Could not connect to FastAPI backend.')
      setHealth(null)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchHealth()
  }, [])

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="logo-badge">📷 Photo Group Portal</div>
        <span className="phase-tag">Day 1 Foundation</span>
      </header>

      <main className="main-content">
        <section className="hero-section">
          <h1>Photo Group Portal</h1>
          <p className="subtitle">
            System Infrastructure & System Health Dashboard
          </p>
        </section>

        <div className="card status-card">
          <div className="card-header">
            <h2>Backend & System Health</h2>
            <button 
              className="refresh-btn" 
              onClick={fetchHealth} 
              disabled={loading}
            >
              {loading ? 'Checking...' : '🔄 Refresh Status'}
            </button>
          </div>

          {loading && (
            <div className="status-loading">
              <div className="spinner"></div>
              <p>Connecting to backend API...</p>
            </div>
          )}

          {error && (
            <div className="status-box error">
              <div className="status-icon">⚠️</div>
              <div className="status-details">
                <h3>Connection Error</h3>
                <p>{error}</p>
                <small>Ensure the FastAPI server is running at <code>http://localhost:8000</code></small>
              </div>
            </div>
          )}

          {health && (
            <div className="health-details">
              <div className="status-badge-row">
                <span className={`status-badge ${health.status === 'healthy' ? 'badge-online' : 'badge-warning'}`}>
                  ● System: {health.status.toUpperCase()}
                </span>
                <span className="status-badge badge-info">
                  Env: {health.environment}
                </span>
                <span className="status-badge badge-info">
                  Version: {health.version}
                </span>
              </div>

              <div className="grid-details">
                <div className="detail-item">
                  <span className="label">Application Name</span>
                  <span className="value">{health.app_name}</span>
                </div>
                <div className="detail-item">
                  <span className="label">Last Updated</span>
                  <span className="value">{new Date(health.timestamp).toLocaleTimeString()}</span>
                </div>
                <div className="detail-item">
                  <span className="label">Database Status</span>
                  <span className={`value ${health.database.status.includes('connected') ? 'text-success' : 'text-danger'}`}>
                    {health.database.status}
                  </span>
                </div>
                <div className="detail-item">
                  <span className="label">Database Dialect</span>
                  <span className="value code">{health.database.dialect}</span>
                </div>
              </div>
            </div>
          )}
        </div>

        <section className="info-cards-grid">
          <div className="card info-card">
            <h3>🐍 Python FastAPI Backend</h3>
            <p>Running RESTful services with Uvicorn, OpenAPI docs, and structured routing.</p>
            <div className="card-footer">
              <a href="http://localhost:8000/docs" target="_blank" rel="noreferrer">
                View API Docs →
              </a>
            </div>
          </div>

          <div className="card info-card">
            <h3>🗄️ SQL / PostgreSQL Engine</h3>
            <p>SQLAlchemy 2.0 connection pool with PostgreSQL support & SQLite fallback.</p>
            <div className="card-footer">
              <a href="http://localhost:8000/api/v1/health" target="_blank" rel="noreferrer">
                Raw JSON Endpoint →
              </a>
            </div>
          </div>

          <div className="card info-card">
            <h3>⚛️ React Frontend</h3>
            <p>Vite-powered React UI with automatic proxy routing and live status feedback.</p>
            <div className="card-footer">
              <span className="footer-tag">Active</span>
            </div>
          </div>
        </section>
      </main>

      <footer className="app-footer">
        <p>Photo Group Portal &copy; Day 1 Foundation — Built with Python, FastAPI, SQL & React</p>
      </footer>
    </div>
  )
}

export default App
