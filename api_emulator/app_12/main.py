from typing import Optional, Union

from fastapi import FastAPI, Header, Path, Query
from pydantic import confloat, conint, constr

from common.factories import create_factory_class

from .models import (
    ChargeDtoRs,
    ConfirmPaymentDtoRq,
    DtoClientProductsRs,
    DtoConfirmPaymentRs,
    DtoRequestPaymentRs,
    ErrorDtoRs,
    PageDtoRsChargeDtoRs,
    PaymentCheckDto,
    PaymentDtoRs,
    RequestPaymentDtoRq,
)

app = FastAPI(
    title="Сервис платежей, оплата штрафов (Хакатон)",
    description="Сервис платежей для оплаты штрафов",
    version="1.0.11",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/pmnt/acceptance/traffic-penalties/hackathon/v1"}],
)


@app.get(
    "/charges",
    response_model=PageDtoRsChargeDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def list(
    sts: Optional[constr(min_length=10, max_length=10)] = None,
    vu: Optional[constr(min_length=10, max_length=10)] = None,
    page_number: Optional[conint(ge=0, le=100)] = Query(0, alias="pageNumber"),
    page_size: Optional[conint(ge=1, le=100)] = Query(30, alias="pageSize"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
) -> Union[PageDtoRsChargeDtoRs, ErrorDtoRs]:
    """
    Запрос поиска начислений по штрафам ГИБДД по СТС или ВУ
    """
    return create_factory_class(PageDtoRsChargeDtoRs).build()


@app.get(
    "/charges/{uin}",
    response_model=ChargeDtoRs,
    responses={
        "400": {"model": ErrorDtoRs},
        "404": {"model": ErrorDtoRs},
        "500": {"model": ErrorDtoRs},
    },
)
def find(
    uin: constr(min_length=20, max_length=25),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
) -> Union[ChargeDtoRs, ErrorDtoRs]:
    """
    Запрос поиска начисления по штрафу ГИБДД по УИН
    """
    return create_factory_class(ChargeDtoRs).build()


@app.get(
    "/payments/check/{payment_id}",
    response_model=PaymentCheckDto,
    responses={
        "400": {"model": ErrorDtoRs},
        "404": {"model": ErrorDtoRs},
        "500": {"model": ErrorDtoRs},
    },
)
def get_payment_check(
    payment_id: constr(min_length=0, max_length=255) = Path(..., alias="paymentId"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
) -> Union[PaymentCheckDto, ErrorDtoRs]:
    """
    Запрос чека по платежу
    """
    return create_factory_class(PaymentCheckDto).build()


@app.post(
    "/payments/confirm",
    response_model=DtoConfirmPaymentRs,
    responses={
        "400": {"model": ErrorDtoRs},
        "404": {"model": ErrorDtoRs},
        "500": {"model": ErrorDtoRs},
    },
)
def confirm(
    x__u_n_c: constr(min_length=0, max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
    x__c_h_a_n_n_e_l: constr(min_length=0, max_length=255) = Header(..., alias="X-CHANNEL"),
    x__t_b__i_d: Optional[constr(min_length=0, max_length=255)] = Header(None, alias="X-TB-ID"),
    x_user_session_id: constr(min_length=0, max_length=255) = Header(..., alias="x-user-session-id"),
    body: ConfirmPaymentDtoRq = ...,
) -> Union[DtoConfirmPaymentRs, ErrorDtoRs]:
    """
    Запрос на подтверждение оплаты штрафа ГИБДД
    """
    return create_factory_class(DtoConfirmPaymentRs).build()


@app.post(
    "/payments/request",
    response_model=DtoRequestPaymentRs,
    responses={
        "400": {"model": ErrorDtoRs},
        "404": {"model": ErrorDtoRs},
        "500": {"model": ErrorDtoRs},
    },
)
def request(
    body: RequestPaymentDtoRq,
    x__u_n_c: constr(min_length=0, max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
    x__c_h_a_n_n_e_l: constr(min_length=0, max_length=255) = Header(..., alias="X-CHANNEL"),
    x__t_b__i_d: Optional[constr(min_length=0, max_length=255)] = Header(None, alias="X-TB-ID"),
) -> Union[DtoRequestPaymentRs, ErrorDtoRs]:
    """
    Запрос на оплату штрафа ГИБДД
    """
    return create_factory_class(DtoRequestPaymentRs).build()


@app.get(
    "/payments/{payment_id}",
    response_model=PaymentDtoRs,
    responses={
        "400": {"model": ErrorDtoRs},
        "404": {"model": ErrorDtoRs},
        "500": {"model": ErrorDtoRs},
    },
)
def get_payment(
    payment_id: constr(min_length=0, max_length=255) = Path(..., alias="paymentId"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
) -> Union[PaymentDtoRs, ErrorDtoRs]:
    """
    Запрос детальной информации по платежу
    """
    return create_factory_class(PaymentDtoRs).build()


@app.get(
    "/products",
    response_model=DtoClientProductsRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def products(
    min_balance: Optional[confloat(ge=0.0, le=1000000.0)] = Query(None, alias="minBalance"),
    x__m_d_m__i_d: constr(min_length=0, max_length=255) = Header(..., alias="X-MDM-ID"),
) -> Union[DtoClientProductsRs, ErrorDtoRs]:
    """
    Старт платежа запрос списка продуктов клиента для старта платежа
    """
    return create_factory_class(DtoClientProductsRs).build()
