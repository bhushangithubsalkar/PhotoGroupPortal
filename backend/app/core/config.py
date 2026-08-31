import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Photo Group Portal")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    PORT: int = int(os.getenv("PORT", 8000))
    HOST: str = os.getenv("HOST", "0.0.0.0")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/photo_group_portal"
    )
    
    STORAGE_DIR: str = os.getenv("STORAGE_DIR", "./storage")
    
    @property
    def cors_origins(self) -> list[str]:
        raw_cors = os.getenv("CORS_ORIGINS")
        if raw_cors:
            try:
                parsed = json.loads(raw_cors)
                if isinstance(parsed, list):
                    return parsed
            except Exception:
                return [origin.strip() for origin in raw_cors.split(",")]
        return [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000",
        ]

    def validate_config(self) -> bool:
        """
        Validates core application configuration.
        Raises ValueError with safe error message if required configuration is invalid.
        """
        if not self.DATABASE_URL or not self.DATABASE_URL.strip():
            raise ValueError("DATABASE_URL configuration is missing or unconfigured.")
        if not self.APP_NAME or not self.APP_NAME.strip():
            raise ValueError("APP_NAME configuration is missing.")
        return True

settings = Settings()
