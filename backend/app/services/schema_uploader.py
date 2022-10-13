from contextlib import contextmanager
from functools import cached_property
from tempfile import NamedTemporaryFile, _TemporaryFileWrapper

import prance
from pydantic import BaseModel

from app import database


def prance_recursion_solver(limit, parsed_url, recursions=()):
    # handle recursive referencing like type(domain.parent) == type(domain)
    return {"title": "recursion_reference", "type": "string", "example": "#ref"}


class SchemaUploader(BaseModel):
    data: str

    class Config:
        keep_untouched = (cached_property,)

    @contextmanager
    def _schema_file(self) -> _TemporaryFileWrapper:
        file = NamedTemporaryFile("w")
        file.write(self.data)
        file.flush()
        yield file
        file.close()

    @cached_property
    def specification(self) -> dict:
        with self._schema_file() as file:
            return prance.ResolvingParser(
                url=file.name, recursion_limit_handler=prance_recursion_solver
            ).specification

    async def get_or_create_api(self) -> database.Api:
        api = await database.Api.find_one(
            database.Api.name == self.specification["info"]["title"],
            fetch_links=True,
        )
        if api is not None:
            return api
        return await database.Api(
            name=self.specification["info"]["title"],
            code=self.specification["info"].get("x-ibm-name", ""),
            url="",
        ).save()

    async def get_or_create_version(self, api: database.Api) -> database.Version:
        version_code: str = self.specification["info"]["version"]
        for version in api.versions:
            if version.code == version_code:
                return version
        version = await database.Version(
            name=f"v{version_code}", code=version_code
        ).save()
        api.versions.append(version)
        await api.save()
        return version

    async def upload(self) -> database.Api:
        api = await self.get_or_create_api()
        version = await self.get_or_create_version(api)
        reference_title = await database.Page(
            name="Введение",
            order=0,
            version=version.id,
        ).save()
        await database.Page(
            name="Описание",
            text_content=self.specification["info"]["description"],
            parent=reference_title.id,
            order=1,
            version=version.id,
        ).save()
        resources_title = await database.Page(
            name="Ресурсы", order=2, version=version.id
        ).save()
        order = 3

        for path, methods in self.specification["paths"].items():
            for method, values in methods.items():
                await database.Page(
                    name=values["summary"],
                    path=path,
                    method=method.upper(),
                    parent=resources_title.id,
                    version=version.id,
                    order=order,
                    operation_id=values["operationId"],
                    text_content=values.get("description", ""),
                    **values,
                ).save()
                order += 1
        return api
