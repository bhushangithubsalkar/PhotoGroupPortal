from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.api.deps import get_db, get_current_user
from backend.app.crud.crud_user import crud_user
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate, UserRead

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Register new user")
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    """
    Create new user. Default role is 'user'.
    """
    user = crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    user = crud_user.create(db, obj_in=user_in)
    return user

@router.get("/me", response_model=UserRead, summary="Get current authenticated user profile")
def read_user_me(
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Get current authenticated user.
    """
    return current_user
