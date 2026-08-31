from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "health_check" in data

def test_api_health_endpoint():
    """Test Day 2 required GET /api/health endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "Photo Group Portal API" in data["service"]

def test_api_health_db_endpoint():
    """Test Day 3 required GET /api/health/db endpoint"""
    response = client.get("/api/health/db")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"

def test_api_health_system_endpoint():
    """Test Day 4 required GET /api/health/system endpoint"""
    response = client.get("/api/health/system")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "Photo Group Portal API" in data["service"]
    assert "environment" in data

def test_api_v1_health_endpoint():
    """Test detailed GET /api/v1/health endpoint"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["app_name"] == "Photo Group Portal"
    assert "database" in data
    assert "timestamp" in data
    assert "version" in data
    assert data["database"]["status"] in ["connected", "connected (sqlite fallback)", "disconnected"]
