from fastapi import APIRouter, Depends

from app import database, schemes
from app.services.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/user/", response_model=schemes.User)
async def get_user(user: database.User = Depends(get_current_user)):
    return user
