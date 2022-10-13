from beanie import Document, Link
from pydantic import Field

from app.database.version import Version


class Api(Document):
    name: str
    code: str
    versions: list[Link[Version]] = Field(default_factory=list)
    url: str

    class Settings:
        name = "api_collection"
