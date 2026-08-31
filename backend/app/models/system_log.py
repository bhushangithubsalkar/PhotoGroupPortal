from sqlalchemy import Column, String, Text
from backend.app.db.base_class import Base

class SystemLog(Base):
    """
    Database model for operational logs, health status events, and system audit messages.
    Inherits id, created_at, updated_at from Base mixin.
    Table name automatically mapped to 'system_log'.
    """
    level = Column(String(20), nullable=False, default="INFO", index=True)
    module = Column(String(100), nullable=False, default="system")
    message = Column(Text, nullable=False)
    details = Column(Text, nullable=True)
