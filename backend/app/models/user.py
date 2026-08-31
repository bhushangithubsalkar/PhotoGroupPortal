from sqlalchemy import Column, String, Boolean
from backend.app.db.base_class import Base

class User(Base):
    """
    User database model for photographers, users, and administrators.
    Inherits id, created_at, updated_at from Base mixin.
    Table name automatically mapped to 'user'.
    """
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default="user", nullable=False, index=True)
    is_active = Column(Boolean, default=True, nullable=False)
