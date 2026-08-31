import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool, create_engine, text
from alembic import context

# Ensure root workspace is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.core.config import settings
from backend.app.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def get_db_url():
    url = settings.DATABASE_URL
    # Test connection to primary URL, fallback to sqlite if PostgreSQL is unreachable in dev/test
    try:
        connect_args = {}
        if url.startswith("sqlite"):
            connect_args = {"check_same_thread": False}
        test_engine = create_engine(url, connect_args=connect_args)
        with test_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return url
    except Exception:
        return "sqlite:///./photo_group_portal_fallback.db"

db_url = get_db_url()
config.set_main_option("sqlalchemy.url", db_url)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        db_url,
        poolclass=pool.NullPool,
        connect_args={"check_same_thread": False} if db_url.startswith("sqlite") else {}
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
