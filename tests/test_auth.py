from uuid import uuid4
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.core.security import get_password_hash, verify_password

client = TestClient(app)

def test_password_hashing_utilities():
    raw_password = "SecretPassword123!"
    hashed = get_password_hash(raw_password)
    assert hashed != raw_password
    assert verify_password(raw_password, hashed) is True
    assert verify_password("WrongPassword!", hashed) is False

def test_user_registration_and_login_flow():
    unique_email = f"auth_user_{uuid4().hex[:8]}@example.com"
    password = "MySecurePassword123!"

    # 1. Register new user
    reg_response = client.post(
        "/api/v1/users/",
        json={
            "email": unique_email,
            "password": password,
            "role": "user"
        }
    )
    assert reg_response.status_code == 201
    user_data = reg_response.json()
    assert user_data["email"] == unique_email
    assert user_data["role"] == "user"
    assert user_data["is_active"] is True
    assert "id" in user_data

    # 2. Attempt duplicate registration -> HTTP 400
    dup_response = client.post(
        "/api/v1/users/",
        json={
            "email": unique_email,
            "password": password
        }
    )
    assert dup_response.status_code == 400
    assert "already exists" in dup_response.json()["error"]["message"]

    # 3. Attempt login with wrong password -> HTTP 400
    bad_login = client.post(
        "/api/v1/auth/login",
        data={
            "username": unique_email,
            "password": "WrongPassword!"
        }
    )
    assert bad_login.status_code == 400

    # 4. Successful login -> Returns JWT Token
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": unique_email,
            "password": password
        }
    )
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    token = token_data["access_token"]

    # 5. Access protected GET /api/v1/users/me without token -> HTTP 401
    unauth_response = client.get("/api/v1/users/me")
    assert unauth_response.status_code == 401

    # 6. Access protected GET /api/v1/users/me with valid Bearer token -> HTTP 200
    auth_response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert auth_response.status_code == 200
    me_data = auth_response.json()
    assert me_data["email"] == unique_email
    assert me_data["role"] == "user"
