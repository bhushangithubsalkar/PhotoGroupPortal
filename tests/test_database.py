from uuid import uuid4
from backend.app.core.database import get_session, init_db, check_database_connection
from backend.app.models.system_log import SystemLog
from backend.app.models.user import User

def test_database_connection():
    db_status = check_database_connection()
    assert "connected" in db_status["status"]

def test_init_db_and_system_log():
    init_db()
    db = get_session()
    try:
        log_entry = SystemLog(
            level="INFO",
            module="test_database",
            message="Database test log entry",
            details="Testing table creation and CRUD operations"
        )
        db.add(log_entry)
        db.commit()
        db.refresh(log_entry)
        
        assert log_entry.id is not None
        assert log_entry.level == "INFO"
        assert log_entry.module == "test_database"
        assert log_entry.created_at is not None
    finally:
        db.close()

def test_user_model_crud():
    init_db()
    db = get_session()
    try:
        unique_email = f"user_{uuid4().hex[:8]}@example.com"
        user = User(
            email=unique_email,
            password_hash="$2b$12$fakehashforunitestonly",
            role="photographer",
            is_active=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        assert user.id is not None
        assert user.email == unique_email
        assert user.role == "photographer"
        assert user.is_active is True
        assert user.created_at is not None
    finally:
        db.close()
