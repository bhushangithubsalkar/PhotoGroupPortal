# Photo Group Portal - Architecture Specification (Day 1)

## Architecture Overview

Photo Group Portal is a full-stack, AI-powered platform enabling photographers to upload event photographs, isolate room collections, and allow end users to retrieve matching personal photos via a WhatsApp selfie workflow.

```
+------------------+         HTTP / REST API          +--------------------+
|  React Frontend  | <------------------------------> |   FastAPI Backend  |
|  (Vite + CSS)    |        /api/v1/health            |   (Python 3.13)    |
+------------------+                                  +---------+----------+
                                                                |
                                                                | SQLAlchemy ORM
                                                                v
                                                     +----------------------+
                                                     | PostgreSQL / SQL DB  |
                                                     | (or SQLite fallback) |
                                                     +----------------------+
```

## Directory Structure

- `backend/`: FastAPI application code
  - `app/main.py`: Main app entrypoint and middleware
  - `app/core/`: Application settings and database setup
  - `app/api/`: API routes (Day 1: `/health`)
- `frontend/`: React frontend (Vite)
  - `src/App.jsx`: Main interface connecting to backend `/api/v1/health`
- `database/`: SQL initialization scripts and database docs
- `docs/`: System documentation
- `tests/`: Automated test suite
- `storage/`: Local image storage directory (originals & thumbnails structure)

## Technology Stack

- **Backend**: Python 3.13 + FastAPI + Uvicorn
- **Database**: PostgreSQL (via SQLAlchemy 2.0 ORM) with automatic SQLite dev fallback
- **Frontend**: React 19 + Vite
- **Testing**: Pytest + FastAPI TestClient
