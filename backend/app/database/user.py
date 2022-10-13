from beanie import Document
from pydantic import EmailStr


class User(Document):
    email: EmailStr
    password_hash: str

    class Settings:
        name = "user_collection"
