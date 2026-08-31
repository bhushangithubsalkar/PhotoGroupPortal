from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings
from backend.app.api.health import router as health_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print(f"Starting {settings.APP_NAME} in {settings.APP_ENV} mode...")
    yield
    # Shutdown actions
    print(f"Shutting down {settings.APP_NAME}...")

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# CORS setup for React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers
app.include_router(health_router, prefix=settings.API_V1_STR, tags=["Health"])

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "health_check": f"{settings.API_V1_STR}/health",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
