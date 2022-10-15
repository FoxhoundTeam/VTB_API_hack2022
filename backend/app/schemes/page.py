from __future__ import annotations

from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from app.database.page import Method, Response


class BasePage(BaseModel):
    id: PydanticObjectId = Field(..., alias="_id")
    name: str
    method: Optional[Method]
    parent: Optional[PydanticObjectId]


class PageTree(BasePage):
    version: PydanticObjectId
    disabled: bool = False
    children: list[PageTree] = Field(default_factory=list)


PageTree.update_forward_refs()


class Page(BasePage):
    path: Optional[str]
    text_content: str = ""
    parameters: Optional[list[dict]]
    responses: Optional[dict[str, Response]]
    need_request: bool = False
    order: int = 0
    produces: Optional[list[str]]
    operation_id: Optional[str] = Field(None, alias="operationId")


class PageRequest(BaseModel):
    id: PydanticObjectId
    headers: dict[str, str] = Field(default_factory=dict)
    data: dict[str, str] = Field(default_factory=dict)
