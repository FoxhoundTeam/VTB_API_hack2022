from enum import Enum
from typing import Optional

from beanie import Document, Indexed, PydanticObjectId
from pydantic import BaseModel, Field


class Method(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class Response(BaseModel):
    description: str
    body: Optional[dict] = Field(None, alias="schema")


class Page(Document):
    name: str
    method: Optional[Method]
    path: Optional[str]
    version: Indexed(PydanticObjectId)
    parent: Optional[Indexed(PydanticObjectId)]
    text_content: str = ""
    parameters: Optional[list[dict]]
    responses: Optional[dict[str, Response]]
    need_request: bool = False
    order: int = 0
    produces: Optional[list[str]]
    operation_id: Optional[str] = Field(None, alias="operationId")

    class Settings:
        name = "page_collection"
