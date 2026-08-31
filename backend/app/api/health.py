from datetime import datetime, timezone
from fastapi import APIRouter
from backend.app.core.config import settings
from backend.app.core.database import check_database_connection

router = APIRouter()

@router.get("/health", summary="Basic Health Check Endpoint")
def get_health():
    """
    Returns basic application health, environment metrics, and database connectivity.
    """
    db_health = check_database_connection()
    
    return {
        "status": "healthy" if "connected" in db_health["status"] else "degraded",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": "0.1.0-day1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "database": db_health
    }
