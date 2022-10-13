from fastapi import APIRouter

from app import database

router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.get("/", response_model=list[database.Api], response_model_by_alias=False)
async def get_apis():
    return await database.Api.find(fetch_links=True).to_list()
