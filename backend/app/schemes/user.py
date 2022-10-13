from beanie import PydanticObjectId
from pydantic import EmailStr, Field

from .base import CamelModel


class BaseUser(CamelModel):
    email: EmailStr


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: PydanticObjectId = Field(..., alias="_id")
