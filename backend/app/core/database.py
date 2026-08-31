import logging
from typing import Generator
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import OperationalError

from backend.app.core.config import settings

logger = logging.getLogger(__name__)

Base = declarative_base()

def get_engine(db_url: str):
    connect_args = {}
    if db_url.startswith("sqlite"):
        connect_args = {"check_same_thread": False}
    return create_engine(
        db_url,
        connect_args=connect_args,
        pool_pre_ping=True,
    )

# Primary database engine initialization
db_url = settings.DATABASE_URL
current_engine = get_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=current_engine)

def check_database_connection() -> dict:
    """
    Ping database connection. Returns status dictionary.
    Includes fallback check to SQLite if PostgreSQL is unreachable in dev/test.
    """
    global current_engine, SessionLocal
    
    try:
        with current_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {
            "status": "connected",
            "dialect": current_engine.dialect.name,
            "url": str(current_engine.url.render_as_string(hide_password=True)),
            "error": None
        }
    except Exception as primary_exc:
        logger.warning(f"Primary DB connection failed ({primary_exc}). Attempting fallback to SQLite...")
        
        # Fallback to local SQLite DB if PostgreSQL connection fails
        fallback_url = "sqlite:///./photo_group_portal_fallback.db"
        try:
            fallback_engine = get_engine(fallback_url)
            with fallback_engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            
            current_engine = fallback_engine
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=fallback_engine)
            
            return {
                "status": "connected (sqlite fallback)",
                "dialect": fallback_engine.dialect.name,
                "url": fallback_url,
                "error": str(primary_exc)
            }
        except Exception as fallback_exc:
            return {
                "status": "disconnected",
                "dialect": "unknown",
                "url": str(primary_exc),
                "error": f"Primary error: {primary_exc}; Fallback error: {fallback_exc}"
            }

def get_db() -> Generator:
    """Dependency for providing database sessions in FastAPI route handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
