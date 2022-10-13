from typing import List, Optional, Union

from fastapi import FastAPI, Header, Query
from pydantic import constr

from common.factories import create_factory_class
from common.models import GenericError

from .models import (
    OpenApiLeadsCheckRequestDto,
    OpenApiLeadsCheckResponseDto,
    OpenApiLeadsImpersonalRequestDto,
    OpenApiLeadsImpersonalResponseDto,
    OpenApiLeadsStatusResponseDto,
)

app = FastAPI(
    title="Дорога лида - ВТБ (Хакатон)",
    description="API для операций с лидами "
    "(заявками на создание юридических лиц для дальнейшей обработки "
    "(звонков, контактов) с целью привлечения клиентов) без использования ПДн.",
    version="1.0.4",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/smb/lecs/lead-impers/hackathon/v1"}],
)


@app.post(
    "/check_leads",
    response_model=OpenApiLeadsCheckResponseDto,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
    description="Проверяет лидов",
)
def check_leads_using_post(
    x__global__transaction__id: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    authorization: str = Header(..., alias="Authorization"),
    body: OpenApiLeadsCheckRequestDto = ...,
) -> Union[OpenApiLeadsCheckResponseDto, GenericError]:
    """
    Проверяет лидов
    """
    return create_factory_class(OpenApiLeadsCheckResponseDto).build()


@app.get(
    "/leads",
    response_model=OpenApiLeadsStatusResponseDto,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "404": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_lead_status_using_get(
    x__global__transaction__id: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    lead_id: Optional[List[int]] = Query(None, alias="leadId"),
    source_lead_id: Optional[List[str]] = Query(None, alias="sourceLeadId", max_length=128),
    authorization: str = Header(..., alias="Authorization"),
) -> Union[OpenApiLeadsStatusResponseDto, GenericError]:
    """
    Получить информацию о лидах
    """
    return create_factory_class(OpenApiLeadsStatusResponseDto).build()


@app.post(
    "/leads_impersonal",
    response_model=OpenApiLeadsImpersonalResponseDto,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def create_leads_using_post(
    x__global__transaction__id: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    authorization: str = Header(..., alias="Authorization"),
    body: OpenApiLeadsImpersonalRequestDto = ...,
) -> Union[OpenApiLeadsImpersonalResponseDto, GenericError]:
    """
    Добавить лиды
    """
    return create_factory_class(OpenApiLeadsImpersonalResponseDto).build()
