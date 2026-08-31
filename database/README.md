# Database Setup & Configuration Guide

## Requirements
- PostgreSQL 14+ (or SQLite fallback for quick testing)

## Local PostgreSQL Initialization

1. Connect to PostgreSQL server via `psql`:
   ```bash
   psql -U postgres
   ```

2. Execute the initialization script:
   ```sql
   \i database/init_db.sql
   ```

3. Ensure the database connection URL in `.env` matches your credentials:
   ```env
   DATABASE_URL="postgresql://postgres:postgres@localhost:5432/photo_group_portal"
   ```

## Automatic Fallback Behavior
If PostgreSQL is offline or credentials are missing during local development or test runs, the SQLAlchemy database manager automatically falls back to SQLite (`sqlite:///./photo_group_portal_fallback.db`) to keep the health check endpoints and application functional.
