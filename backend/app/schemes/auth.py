from pydantic import EmailStr

from .base import CamelModel


class Token(CamelModel):
    access_token: str


class Credentials(CamelModel):
    email: EmailStr
    password: str


class ChangePassword(CamelModel):
    password: str
