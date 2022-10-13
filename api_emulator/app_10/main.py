from typing import List, Optional, Union

from fastapi import FastAPI, Header, Path, Query
from pydantic import confloat, constr

from common.factories import create_factory_class

from .models import (
    XCHANNEL2,
    XCHANNEL5,
    XCHANNEL8,
    XCHANNEL11,
    XCHANNEL14,
    XCHANNEL17,
    ClientProductsDtoRs,
    ConfirmPaymentDtoRq,
    ConfirmPaymentDtoRs,
    ErrorDtoRs,
    PaymentCheckDtoRs,
    PaymentDtoRs,
    RequestPaymentDtoRq,
    RequestPaymentDtoRs,
    StartPaymentDtoRq,
    StartPaymentDtoRs,
)

app = FastAPI(
    title="Сервис платежей с базовым сценарием оплаты (Хакатон)",
    description="Сервис универсальных платежей",
    version="1.0.10",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/pmnt/acceptance/universal/hackathon/v1"}],
)


@app.post(
    "/payments/confirm",
    response_model=ConfirmPaymentDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def confirm(
    x__u_n_c: constr(max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(max_length=255) = Header(..., alias="X-MDM-ID"),
    x__t_b__i_d: Optional[constr(max_length=255)] = Header(None, alias="X-TB-ID"),
    x__u_s_e_r__s_e_s_s_i_o_n__i_d: constr(max_length=255) = Header(..., alias="X-USER-SESSION-ID"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=255) = Header(..., alias="X-PARTNER-ID"),
    x__l_o_g_i_n__m_o_d_e: constr(max_length=255) = Header(..., alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: List[constr(max_length=255)] = Header(..., alias="X-ROLES"),
    x__c_h_a_n_n_e_l: XCHANNEL2 = Header(..., alias="X-CHANNEL"),
    body: ConfirmPaymentDtoRq = ...,
) -> Union[ConfirmPaymentDtoRs, ErrorDtoRs]:
    """
    Запрос на оплату универсального платежа
    """
    return create_factory_class(ConfirmPaymentDtoRs).build()


@app.post(
    "/payments/request",
    response_model=RequestPaymentDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def request(
    x__u_n_c: constr(max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(max_length=255) = Header(..., alias="X-MDM-ID"),
    x__t_b__i_d: Optional[constr(max_length=255)] = Header(None, alias="X-TB-ID"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=255) = Header(..., alias="X-PARTNER-ID"),
    x__l_o_g_i_n__m_o_d_e: constr(max_length=255) = Header(..., alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: List[constr(max_length=255)] = Header(..., alias="X-ROLES"),
    x__c_h_a_n_n_e_l: XCHANNEL5 = Header(..., alias="X-CHANNEL"),
    body: RequestPaymentDtoRq = ...,
) -> Union[RequestPaymentDtoRs, ErrorDtoRs]:
    """
    Запрос на оплату универсального платежа
    """
    return create_factory_class(RequestPaymentDtoRs).build()


@app.post(
    "/payments/start",
    response_model=StartPaymentDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def start(
    x__u_n_c: constr(max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(max_length=255) = Header(..., alias="X-MDM-ID"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=255) = Header(..., alias="X-PARTNER-ID"),
    x__l_o_g_i_n__m_o_d_e: constr(max_length=255) = Header(..., alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: List[constr(max_length=255)] = Header(..., alias="X-ROLES"),
    x__c_h_a_n_n_e_l: XCHANNEL8 = Header(..., alias="X-CHANNEL"),
    body: StartPaymentDtoRq = ...,
) -> Union[StartPaymentDtoRs, ErrorDtoRs]:
    """
    Запрос на старт оплаты универсального платежа
    """
    return create_factory_class(StartPaymentDtoRs).build()


@app.get(
    "/payments/{payment_id}",
    response_model=PaymentDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def get_payment(
    x__u_n_c: constr(max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(max_length=255) = Header(..., alias="X-MDM-ID"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=255) = Header(..., alias="X-PARTNER-ID"),
    x__l_o_g_i_n__m_o_d_e: constr(max_length=255) = Header(..., alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: List[constr(max_length=255)] = Header(..., alias="X-ROLES"),
    x__c_h_a_n_n_e_l: XCHANNEL11 = Header(..., alias="X-CHANNEL"),
    payment_id: constr(max_length=36) = Path(..., alias="paymentId"),
) -> Union[PaymentDtoRs, ErrorDtoRs]:
    """
    Запрос детальной информации по универсальному платежу
    """
    return create_factory_class(PaymentDtoRs).build()


@app.get(
    "/payments/{payment_id}/check",
    response_model=PaymentCheckDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def get_payment_check(
    x__u_n_c: constr(max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(max_length=255) = Header(..., alias="X-MDM-ID"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=255) = Header(..., alias="X-PARTNER-ID"),
    x__l_o_g_i_n__m_o_d_e: constr(max_length=255) = Header(..., alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: List[constr(max_length=255)] = Header(..., alias="X-ROLES"),
    x__c_h_a_n_n_e_l: XCHANNEL14 = Header(..., alias="X-CHANNEL"),
    payment_id: constr(max_length=36) = Path(..., alias="paymentId"),
) -> Union[PaymentCheckDtoRs, ErrorDtoRs]:
    """
    Запрос чека по универсальному платежу
    """
    return create_factory_class(PaymentCheckDtoRs).build()


@app.get(
    "/products",
    response_model=ClientProductsDtoRs,
    responses={"400": {"model": ErrorDtoRs}, "500": {"model": ErrorDtoRs}},
)
def get_client_products(
    x__u_n_c: constr(max_length=255) = Header(..., alias="X-UNC"),
    x__m_d_m__i_d: constr(max_length=255) = Header(..., alias="X-MDM-ID"),
    x__p_a_r_t_n_e_r__i_d: constr(max_length=255) = Header(..., alias="X-PARTNER-ID"),
    x__l_o_g_i_n__m_o_d_e: constr(max_length=255) = Header(..., alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: List[constr(max_length=255)] = Header(..., alias="X-ROLES"),
    x__c_h_a_n_n_e_l: XCHANNEL17 = Header(..., alias="X-CHANNEL"),
    min_balance: Optional[confloat(ge=0.0, le=9007199254740991.0)] = Query(0.0, alias="minBalance"),
) -> Union[ClientProductsDtoRs, ErrorDtoRs]:
    """
    Получение списка продуктов, доступных для оплаты универсальных платежей
    """
    return create_factory_class(ClientProductsDtoRs).build()
