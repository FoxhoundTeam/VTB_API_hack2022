from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from app import schemes
from app.services.page import PageService

router = APIRouter(
    prefix="/page",
    tags=["page"],
)


@router.get("/", response_model=list[schemes.Page], response_model_by_alias=False)
async def get_pages(version: PydanticObjectId, page_service: PageService = Depends()):
    return await page_service.get_pages(version)


@router.get(
    "/tree/", response_model=list[schemes.PageTree], response_model_by_alias=False
)
async def get_pages_tree(
    version: PydanticObjectId, page_service: PageService = Depends()
):
    return await page_service.get_pages_tree(version)
