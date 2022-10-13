from fastapi import APIRouter, Depends, status

from app import database, schemes
from app.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post(
    "/sign-in/",
    response_model=schemes.Token,
)
async def sign_in(
    auth_data: schemes.Credentials,
    auth_service: AuthService = Depends(),
):
    return await auth_service.authenticate_user(auth_data.email, auth_data.password)


@router.post(
    "/change-password/",
    status_code=status.HTTP_200_OK,
)
async def change_password(
    data: schemes.ChangePassword,
    auth_service: AuthService = Depends(),
    user: database.User = Depends(get_current_user),
):
    await auth_service.change_password(data, user)
