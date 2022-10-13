from typing import Optional, Union

from fastapi import FastAPI, Header, Path
from pydantic import constr

from common.factories import create_factory_class

from .models import CardInfoResponse, CardStatusRequest, GenericError, PinCardRequest

app = FastAPI(
    title="Сервис управления картой ФЛ, операционные запросы (Хакатон)",
    description="Микросервис, реализующий базовые операции с банковскими картами",
    version="1.0.2",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/dks/cardops/hackathon/v1"}],
)


@app.post(
    "/close/{public_id}",
    response_model=None,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "415": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def update_close_card(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
) -> Union[None, GenericError]:
    """
    Закрытие карты при нулевом балансе
    """
    pass


@app.post(
    "/pin/{public_id}",
    response_model=CardInfoResponse,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "415": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def update_card_pin(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
    body: PinCardRequest = ...,
) -> Union[CardInfoResponse, GenericError]:
    """
    Установка/смена пин-кода для карты
    """
    return create_factory_class(CardInfoResponse).build()


@app.put(
    "/status/{public_id}",
    response_model=CardInfoResponse,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "415": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "502": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def update_card_option(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
    body: CardStatusRequest = ...,
) -> Union[CardInfoResponse, GenericError]:
    """
    Блокировка/разблокировка карты Way4
    """
    return create_factory_class(CardInfoResponse).build()
