from typing import Optional, Union

from fastapi import FastAPI, Header, Path
from pydantic import constr

from common.factories import create_factory_class

from .models import (
    AcceptancePaymentDtoRq,
    AcceptancePaymentDtoRs,
    ClientProductsDtoRq,
    ClientProductsDtoRs,
    ConfirmPaymentDtoRq,
    ConfirmPaymentDtoRs,
    GenericError,
    MobileNumberDto,
    MobileNumberDtoRs,
    MobilePaymentCheckDto,
    PaymentDtoRs,
    StartPaymentDtoRq,
    StartPaymentDtoRs,
)

app = FastAPI(
    title="Сервис платежей сотовому оператору (Хакатон)",
    description="Сервис платежей операторам сотовой связи",
    version="1.0.3",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/pmnt/acceptance/mobile/hackathon/v1"}],
)


@app.post(
    "/payments/confirm",
    response_model=ConfirmPaymentDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def confirm(
    x__u_n_c: constr(min_length=0, max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
    x__c_l_i_e_n_t__c_h_a_n_n_e_l: constr(min_length=0, max_length=255) = Header(..., alias="X-CLIENT-CHANNEL"),
    x__t_b__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-TB-ID"),
    x_user_session_id: constr(min_length=0, max_length=255) = Header(..., alias="x-user-session-id"),
    x__c_l_i_e_n_t__i_n_t_e_r_a_c_t_i_o_n: Optional[constr(min_length=0, max_length=255)] = Header(
        None, alias="X-CLIENT-INTERACTION"
    ),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    body: ConfirmPaymentDtoRq = ...,
) -> Union[ConfirmPaymentDtoRs, GenericError]:
    """
    Запрос на подтверждение оплаты номера мобильного телефона
    """
    return create_factory_class(ConfirmPaymentDtoRs).build()


@app.post(
    "/payments/request",
    response_model=AcceptancePaymentDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def request(
    x__unc: constr(min_length=0, max_length=255) = Header(..., alias="X-UNC"),
    x__mdm__id: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
    x__client__channel: constr(min_length=0, max_length=255) = Header(..., alias="X-CLIENT-CHANNEL"),
    x__tb__id: constr(min_length=0, max_length=255) = Header(..., alias="X-TB-ID"),
    x__global__transaction__id: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    body: AcceptancePaymentDtoRq = ...,
) -> Union[AcceptancePaymentDtoRs, GenericError]:
    """
    Запрос на оплату номера мобильного телефона
    """
    return create_factory_class(AcceptancePaymentDtoRs).build()


@app.post(
    "/payments/start",
    response_model=StartPaymentDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def start_payment(
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    body: StartPaymentDtoRq = ...,
) -> Union[StartPaymentDtoRs, GenericError]:
    """
    Запрос для старта платежа
    """
    return create_factory_class(StartPaymentDtoRs).build()


@app.get(
    "/payments/{payment_id}",
    response_model=PaymentDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_payment(
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
    payment_id: constr(min_length=0, max_length=255) = Path(..., alias="paymentId"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
) -> Union[PaymentDtoRs, GenericError]:
    """
    Запрос детальной информации по платежу
    """
    return create_factory_class(PaymentDtoRs).build()


@app.get(
    "/payments/{payment_id}/check",
    response_model=MobilePaymentCheckDto,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_payment_check(
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
    payment_id: constr(min_length=0, max_length=255) = Path(..., alias="paymentId"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
) -> Union[MobilePaymentCheckDto, GenericError]:
    """
    Запрос чека по платежу
    """
    return create_factory_class(MobilePaymentCheckDto).build()


@app.post(
    "/phones/info",
    response_model=MobileNumberDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_mobile_number_info(
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    body: MobileNumberDto = ...,
) -> Union[MobileNumberDtoRs, GenericError]:
    """
    Получение параметров сотового оператора для указанного номера телефона
    """
    return create_factory_class(MobileNumberDtoRs).build()


@app.post(
    "/products",
    response_model=ClientProductsDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_client_products(
    x__m_d_m__i_d: constr(min_length=1, max_length=255) = Header(..., alias="X-MDM-ID"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
    body: ClientProductsDtoRq = ...,
) -> Union[ClientProductsDtoRs, GenericError]:
    """
    Получение списка продуктов, доступных для оплаты сотового платежа
    """
    return create_factory_class(ClientProductsDtoRs).build()
