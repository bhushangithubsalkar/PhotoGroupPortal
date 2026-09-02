from fastapi import APIRouter
from backend.app.api.v1.endpoints import auth, users

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_v1_router.include_router(users.router, prefix="/users", tags=["Users"])
