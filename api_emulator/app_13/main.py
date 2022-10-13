from typing import Optional, Union

from fastapi import FastAPI, Header, Path
from pydantic import constr

from common.factories import create_factory_class

from .models import GenericError, Order, OrderResponse, PreliminaryCommissionResponse, Status

app = FastAPI(
    title="Банковские гарантии Комита - ВТБ (Хакатон)",
    description="API работы с заявками на банковские гарантии в системе MOOS",
    version="1.0.2",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/smb/grnt/bg/hackathon/v1"}],
)


@app.post(
    "/order",
    response_model=OrderResponse,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def create_order_using_p_o_s_t(
    x__global__transaction__i_d: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    authorization: str = Header(..., alias="Authorization"),
    body: Order = ...,
) -> Union[OrderResponse, GenericError]:
    """
    Создать заявку
    """
    return create_factory_class(OrderResponse).build()


@app.get(
    "/order/{order_id}",
    response_model=Status,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "404": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_order_using_g_e_t(
    x__global__transaction__i_d: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    authorization: str = Header(..., alias="Authorization"),
    order_id: constr(max_length=255) = Path(..., alias="orderId"),
) -> Union[Status, GenericError]:
    """
    Получить статус заявки
    """
    return create_factory_class(Status).build()


@app.put(
    "/order/{order_id}",
    response_model=None,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "404": {"model": Status},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def update_order_using_p_u_t(
    x__global__transaction__i_d: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    authorization: str = Header(..., alias="Authorization"),
    order_id: constr(max_length=255) = Path(..., alias="orderId"),
    body: Order = ...,
) -> Union[None, GenericError, Status]:
    """
    Обновить заявку
    """
    return create_factory_class(Status).build()


@app.post(
    "/preliminaryPrice",
    response_model=PreliminaryCommissionResponse,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "403": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def preliminary_price_using_p_o_s_t(
    x__global__transaction__i_d: Optional[constr(min_length=1, max_length=24)] = Header(
        None, alias="X-Global-Transaction-ID"
    ),
    authorization: str = Header(..., alias="Authorization"),
    body: Order = ...,
) -> Union[PreliminaryCommissionResponse, GenericError]:
    """
    Получить предварительный расчет комиссии
    """
    return create_factory_class(PreliminaryCommissionResponse).build()
