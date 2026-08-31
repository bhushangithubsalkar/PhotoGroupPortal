import logging
from typing import Generator
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from backend.app.core.config import settings

logger = logging.getLogger("photo_group_portal")

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
_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=current_engine)

def get_session():
    """Returns a new DB session bound to the active engine."""
    global current_engine, _session_factory
    return _session_factory()

def check_database_connection() -> dict:
    """
    Ping database connection. Returns status dictionary.
    Includes fallback check to SQLite if PostgreSQL is unreachable in dev/test.
    """
    global current_engine, _session_factory
    
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
        
        fallback_url = "sqlite:///./photo_group_portal_fallback.db"
        try:
            fallback_engine = get_engine(fallback_url)
            with fallback_engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            
            current_engine = fallback_engine
            _session_factory = sessionmaker(autocommit=False, autoflush=False, bind=fallback_engine)
            
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

def init_db():
    """
    Initialize database tables defined in SQLAlchemy models.
    """
    from backend.app.models import Base
    db_status = check_database_connection()
    if "connected" in db_status["status"]:
        try:
            Base.metadata.create_all(bind=current_engine)
            logger.info(f"Database tables initialized on {current_engine.dialect.name}.")
        except Exception as e:
            logger.error(f"Failed to create database tables: {e}")

def get_db() -> Generator:
    """Dependency for providing database sessions in FastAPI route handlers."""
    db = get_session()
    try:
        yield db
    finally:
        db.close()
