import pytest
from backend.app.core.config import Settings

def test_settings_default_values():
    settings = Settings()
    assert settings.APP_NAME == "Photo Group Portal"
    assert settings.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    assert settings.validate_config() is True

def test_settings_invalid_config():
    settings = Settings()
    settings.DATABASE_URL = ""
    with pytest.raises(ValueError) as exc_info:
        settings.validate_config()
    assert "DATABASE_URL configuration is missing" in str(exc_info.value)
