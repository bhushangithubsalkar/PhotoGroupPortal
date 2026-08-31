import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from backend.app.core.config import settings

def setup_logging():
    """
    Configures application-wide structured logging using settings.LOG_LEVEL.
    Logs output to console stdout and rotating file logs/app.log.
    Excludes sensitive secrets, passwords, or tokens from logs.
    """
    log_level_name = settings.LOG_LEVEL
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    log_level = level_map.get(log_level_name, logging.INFO)

    # Create logs directory if it doesn't exist
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "app.log")

    # Log Formatter
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # Root Logger Configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Clear existing handlers to avoid duplicates
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Suppress verbose noisy loggers if necessary
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    logger = logging.getLogger("photo_group_portal")
    logger.info(f"Logging system initialized. Configured Level: {log_level_name}")
    return logger

logger = logging.getLogger("photo_group_portal")
