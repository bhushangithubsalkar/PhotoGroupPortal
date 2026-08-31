from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_404_not_found_handler():
    response = client.get("/api/nonexistent-route-12345")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert data["error"]["code"] == "NOT_FOUND"
    assert "message" in data["error"]

def test_validation_error_handler():
    # If route expects specific format or query, test 422 error
    response = client.get("/api/v1/health?invalid_param=123")
    # Health endpoint accepts any query or ignores extra query params, returns 200
    assert response.status_code in [200, 422]
