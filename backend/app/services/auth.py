import json
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from jose import JWTError, jwt
from passlib.hash import bcrypt
from pydantic import ValidationError

from app import database, schemes
from app.config import settings

JWTHeader = APIKeyHeader(name="Authorization")


async def get_current_user(
    token: str = Depends(JWTHeader),
) -> database.User:
    user = await database.User.find_one(
        database.User.email == AuthService.verify_token(token).email
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
    return user


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def verify_token(cls, token: str) -> schemes.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get("user")

        try:
            user = schemes.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: database.User) -> schemes.Token:
        now = datetime.utcnow()
        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(seconds=settings.jwt_expires_s),
            "sub": str(user.id),
            "user": json.loads(user.json(include={"id", "email"})),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return schemes.Token(access_token=token)

    async def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> schemes.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

        user = await database.User.find_one(database.User.email == email)

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)

    async def change_password(self, data: schemes.ChangePassword, user: database.User):
        user.password_hash = self.hash_password(data.password)
        await user.save()
