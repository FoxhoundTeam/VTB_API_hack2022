import motor.motor_asyncio
from beanie import init_beanie

from app.config import settings
from app.database.api import Api
from app.database.page import Page
from app.database.user import User
from app.database.version import Version


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.database_uri)

    await init_beanie(
        database=client.db_name, document_models=[Api, User, Version, Page]
    )
