import requests
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from app import database, schemes
from app.services.auth import get_current_user
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


@router.post("/make_request/")
async def make_request(
    request_data: schemes.PageRequest, user: schemes.User = Depends(get_current_user)
):
    page = await database.Page.get(document_id=request_data.id)
    api = await database.Api.find_one(page.version in database.Api.versions)
    try:
        response = requests.request(
            page.method, api.url + page.path, params=request_data.query_params
        )
    except:
        pass
