from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "health_check" in data

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["app_name"] == "Photo Group Portal"
    assert "database" in data
    assert "timestamp" in data
    assert "version" in data
    assert data["database"]["status"] in ["connected", "connected (sqlite fallback)", "disconnected"]
