from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.core.database import check_database_connection, get_db
from backend.app.models.system_log import SystemLog

router = APIRouter()

@router.get("/health", summary="Basic API Liveness Endpoint")
def get_basic_health():
    """
    Liveness probe: Indicates that the FastAPI application process is running.
    """
    return {
        "status": "ok",
        "service": f"{settings.APP_NAME} API"
    }

@router.get("/health/db", summary="Database Connection Health Endpoint")
def get_db_health():
    """
    Database health probe: Verifies application connectivity with SQL/PostgreSQL database.
    """
    db_check = check_database_connection()
    is_connected = "connected" in db_check["status"]
    
    return {
        "status": "ok" if is_connected else "error",
        "database": "connected" if is_connected else "disconnected"
    }

@router.get("/health/system", summary="System Information Health Endpoint")
def get_system_health():
    """
    System health probe: Returns safe process metadata and environment without exposing secrets.
    """
    return {
        "status": "ok",
        "service": f"{settings.APP_NAME} API",
        "environment": settings.APP_ENV
    }

@router.get("/v1/health", summary="Detailed Health Check Endpoint")
def get_detailed_health(db: Session = Depends(get_db)):
    """
    Detailed health check: Returns app metrics, environment, SQL connectivity, and DB log count.
    """
    db_health = check_database_connection()
    
    # Try recording operational health log to database
    total_logs = 0
    try:
        log_entry = SystemLog(
            level="INFO",
            module="health",
            message="Health check queried",
            details=f"Status: {db_health['status']}"
        )
        db.add(log_entry)
        db.commit()
        
        # Count total health logs stored
        total_logs = db.query(SystemLog).count()
    except Exception:
        db.rollback()

    return {
        "status": "healthy" if "connected" in db_health["status"] else "degraded",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": "0.4.0-day4",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "database": db_health,
        "metrics": {
            "total_system_logs": total_logs
        }
    }
