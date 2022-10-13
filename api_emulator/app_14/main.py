from typing import Optional, Union

from fastapi import FastAPI, Header, Path
from pydantic import constr

from common.factories import create_factory_class

from .models import CredentialsResponse, CvvResponse, GenerateWalletTokenRequest, GenericError, TokensDto

app = FastAPI(
    title="Сервис управления картой ФЛ, информационные запросы (Хакатон)",
    description="Микросервис, реализующий базовые операции с банковскими картами",
    version="1.0.2",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/dks/cardinfo/hackathon/v1"}],
)


@app.get(
    "/credentials/{public_id}",
    response_model=CredentialsResponse,
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
def get_credentials(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    client_open_key: constr(max_length=404) = Header(..., alias="clientOpenKey"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
) -> Union[CredentialsResponse, GenericError]:
    """
    Получение реквизитов карты
    """
    return create_factory_class(CredentialsResponse).build()


@app.get(
    "/cvv/{public_id}",
    response_model=CvvResponse,
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
def get_cvv(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    client_open_key: constr(max_length=404) = Header(..., alias="clientOpenKey"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
) -> Union[CvvResponse, GenericError]:
    """
    Получение кода CVV карты
    """
    return create_factory_class(CvvResponse).build()


@app.post(
    "/token/{public_id}",
    response_model=TokensDto,
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
def update_tokenize(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
    body: GenerateWalletTokenRequest = ...,
) -> Union[TokensDto, GenericError]:
    """
    Токенизация карты
    """
    return create_factory_class(TokensDto).build()


@app.get(
    "/tokens/{public_id}",
    response_model=TokensDto,
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
def get_tokens(
    public_id: constr(max_length=50) = Path(..., alias="publicId"),
    x__mdm__id: constr(max_length=50) = Header(..., alias="X-Mdm-Id"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    x_client_channel: constr(max_length=50) = Header(..., alias="x-client-channel"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=50) = Header(..., alias="X-PARTNER-ID"),
) -> Union[TokensDto, GenericError]:
    """
    Получение токенов карты
    """
    return create_factory_class(TokensDto).build()
