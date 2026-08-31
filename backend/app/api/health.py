from datetime import datetime, timezone
from fastapi import APIRouter
from backend.app.core.config import settings
from backend.app.core.database import check_database_connection

router = APIRouter()

@router.get("/health", summary="Basic API Health Endpoint")
def get_basic_health():
    """
    Returns standard Day 2 status object for frontend connection checks.
    """
    return {
        "status": "ok",
        "service": f"{settings.APP_NAME} API"
    }

@router.get("/v1/health", summary="Detailed Health Check Endpoint")
def get_detailed_health():
    """
    Returns application health, environment metrics, and SQL database connectivity.
    """
    db_health = check_database_connection()
    
    return {
        "status": "healthy" if "connected" in db_health["status"] else "degraded",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": "0.2.0-day2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "database": db_health
    }
