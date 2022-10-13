from __future__ import annotations

from typing import Optional, Union

from fastapi import FastAPI, Header
from pydantic import constr

from .models import CardInfoResponse, CardOpenRequest, GenericError

app = FastAPI(
    title="Сервис управления картой ФЛ, эмиссионные запросы (Хакатон)",
    description="Микросервис, реализующий базовые операции с банковскими картами",
    version="1.0.2",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/dks/cardemission/hackathon/v1"}],
)


@app.post(
    "/prepaid",
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
def update_create_card(
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
    body: CardOpenRequest = ...,
) -> Union[CardInfoResponse, GenericError]:
    """
    Открытие карты
    """
    pass
