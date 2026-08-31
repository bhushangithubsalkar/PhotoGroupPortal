# Day 1 Setup & Verification Guide

Follow these instructions to run and verify the Day 1 foundation.

## 1. Prerequisites
- Python 3.10+
- Node.js 18+ & npm
- PostgreSQL (optional for local testing, fallback to SQLite is included)

## 2. Backend Setup & Startup

1. Activate virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. Run backend server:
   ```powershell
   .\venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --port 8000
   ```
   The backend API will be available at: `http://localhost:8000`  
   Interactive API docs: `http://localhost:8000/docs`  
   Health Check API: `http://localhost:8000/api/v1/health`

## 3. Run Smoke Tests

Run the test suite to verify health routes and database connectivity:
```powershell
.\venv\Scripts\python.exe -m pytest tests/ -v
```

## 4. Frontend Setup & Startup

1. Open a new terminal in the `frontend` directory:
   ```powershell
   cd frontend
   npm install
   npm run dev
   ```
2. Open your browser at: `http://localhost:5173`
   The UI will connect to `http://localhost:8000/api/v1/health` and display real-time backend and database status.
