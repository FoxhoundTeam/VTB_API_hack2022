from fastapi import APIRouter, UploadFile
from app.services.schema_uploader import SchemaUploader

from app import database

router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.get("/", response_model=list[database.Api], response_model_by_alias=False)
async def get_apis():
    return await database.Api.find(fetch_links=True).to_list()

@router.post("/upload/", response_model=database.Api, response_model_by_alias=False)
async def upload_swagger(file: UploadFile):
    uploader = SchemaUploader(data=file.file.read())
    return await uploader.upload()
