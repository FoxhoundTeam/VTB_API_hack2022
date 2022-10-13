from typing import Optional
from uuid import UUID

from fastapi import FastAPI, Header, Path, Query
from pydantic import confloat, conint, constr
from starlette.requests import Request

from common.factories import create_factory_class

from .models import (
    AuthResponse,
    ContentType2,
    ContentType5,
    ContentType8,
    ContentType11,
    ContentType14,
    CrossTransferPublicRequest,
    CrossTransferRequest,
    ExchangeTransferPublicRequest,
    ExchangeTransferRequest,
    Language2,
    ResponseResultBlockchainTransactionResponse,
    ResponseResultBoolean,
    ResponseResultCountryView,
    ResponseResultCrossTransactionCrossRoutesView,
    ResponseResultCrossTransactionCrossRouteView,
    ResponseResultCrossTransactionDetailsView,
    ResponseResultCrossTransactionExchangeRouteView,
    ResponseResultCrossTransactionView,
    ResponseResultExchangeTransactionView,
    ResponseResultListCountryView,
    ResponseResultPagingResultCountryView,
    ResponseResultPagingResultCrossTransactionView,
    ResponseResultPagingResultExchangeTransactionView,
    ResponseResultRoutingView,
)

app = FastAPI(
    title="Блокчейн: проведение трансграничных переводов (Хакатон)",
    description="Трансграничный перевод представляет собой конверсионную или кросс-валютную операцию движения денежных средств с аккаунта отправителя перевода на аккаунт получателя перевода при условии, что аккаунт отправителя и аккаунт получателя перевода опубликованы банками, зарегистрированными в разных странах. Трансграничный перевод осуществляется через цепочку комиссионных и конверсионных контрактов, размещенных любыми участниками ЦРС, включающую один или несколько конверсионных контрактов, а также входящий и исходящий комиссионный контракт.",
    contact={},
    version="1.0.2",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/api/v1/manage/cross-transaction"}],
)


@app.post("/auth/oauth/token", response_model=AuthResponse)
def get_token(
    request: Request,
    content__type: Optional[ContentType2] = Header(None, alias="Content-Type"),
) -> AuthResponse:
    """
    getToken
    """
    return create_factory_class(AuthResponse).build()


@app.post(
    "/cross-transaction/public/exchange/transfer",
    response_model=ResponseResultExchangeTransactionView,
)
def exchange_transfer(
    body: ExchangeTransferPublicRequest,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
    content__type: Optional[ContentType11] = Header(None, alias="Content-Type"),
) -> ResponseResultExchangeTransactionView:
    """
    exchangeTransfer
    """
    return create_factory_class(ResponseResultExchangeTransactionView).build()


@app.get(
    "/manage/cross-transaction/country/{language}",
    response_model=ResponseResultPagingResultCountryView,
)
def get_page_2(
    language: conint(ge=0, le=7),
    page_index: conint(ge=0) = Query(..., alias="pageIndex"),
    page_size: Optional[conint(ge=1)] = Query(20, alias="pageSize"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultPagingResultCountryView:
    """
    getPage_2
    """
    return create_factory_class(ResponseResultPagingResultCountryView).build()


@app.get(
    "/manage/cross-transaction/country/{language}/all",
    response_model=ResponseResultListCountryView,
)
def get_list(
    language: conint(ge=0, le=7), f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")
) -> ResponseResultListCountryView:
    """
    getList
    """
    return create_factory_class(ResponseResultListCountryView).build()


@app.get(
    "/manage/cross-transaction/country/{language}/alpha2/{alpha2}",
    response_model=ResponseResultCountryView,
)
def get_by_alpha2(
    language: conint(ge=0, le=7),
    alpha2: constr(min_length=2, max_length=2) = ...,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCountryView:
    """
    getByAlpha2
    """
    return create_factory_class(ResponseResultCountryView).build()


@app.get(
    "/manage/cross-transaction/country/{language}/alpha3/{alpha3}",
    response_model=ResponseResultCountryView,
)
def get_by_alpha3(
    language: Language2,
    alpha3: constr(min_length=3, max_length=3) = ...,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCountryView:
    """
    getByAlpha3
    """
    return create_factory_class(ResponseResultCountryView).build()


@app.get(
    "/manage/cross-transaction/country/{language}/{code}",
    response_model=ResponseResultCountryView,
)
def get_by_code(
    language: conint(ge=0, le=7),
    code: conint(ge=1, le=1000) = ...,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCountryView:
    """
    getByCode
    """
    return create_factory_class(ResponseResultCountryView).build()


@app.get(
    "/manage/cross-transaction/cross",
    response_model=ResponseResultPagingResultCrossTransactionView,
)
def get_page_1(
    is_outbound: Optional[bool] = Query(None, alias="isOutbound"),
    is_inbound: Optional[bool] = Query(None, alias="isInbound"),
    state: Optional[conint(ge=0, le=7)] = None,
    start_date: Optional[int] = Query(None, alias="startDate"),
    end_date: Optional[int] = Query(None, alias="endDate"),
    query: Optional[constr(min_length=0, max_length=1024)] = None,
    page_index: conint(ge=0) = Query(..., alias="pageIndex"),
    page_size: Optional[conint(ge=1)] = Query(20, alias="pageSize"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultPagingResultCrossTransactionView:
    """
    getPage_1
    """
    return create_factory_class(ResponseResultPagingResultCrossTransactionView).build()


@app.post("/manage/cross-transaction/cross/all/decode", response_model=ResponseResultBoolean)
def decode_all(f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")) -> ResponseResultBoolean:
    """
    decodeAll
    """
    return create_factory_class(ResponseResultBoolean).build()


@app.get(
    "/manage/cross-transaction/cross/customer/routes",
    response_model=ResponseResultCrossTransactionCrossRoutesView,
    responses={"404": {"model": ResponseResultCrossTransactionCrossRoutesView}},
)
def get_best_cross_routes_by_customer_1(
    amount: confloat(ge=0.0),
    currency_code_from: conint(ge=0, le=999) = Query(..., alias="currencyCodeFrom"),
    currency_code_to: conint(ge=0, le=999) = Query(..., alias="currencyCodeTo"),
    type: conint(ge=0, le=2) = ...,
    country_code: Optional[constr(min_length=3, max_length=3)] = Query(None, alias="countryCode"),
    customer_identifier: constr(regex=r"^[0-9a-z]{64}$") = Query(..., alias="customerIdentifier"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCrossTransactionCrossRoutesView:
    """
    getBestCrossRoutesByCustomer_1
    """
    return create_factory_class(ResponseResultCrossTransactionCrossRoutesView).build()


@app.get(
    "/manage/cross-transaction/cross/route",
    response_model=ResponseResultCrossTransactionCrossRouteView,
    responses={"404": {"model": ResponseResultCrossTransactionCrossRouteView}},
)
def get_best_cross_route_1(
    amount: confloat(ge=0.0),
    currency_code_from: conint(ge=0, le=999) = Query(..., alias="currencyCodeFrom"),
    currency_code_to: conint(ge=0, le=999) = Query(..., alias="currencyCodeTo"),
    cross_member_address_from: str = Query(..., alias="crossMemberAddressFrom"),
    cross_member_address_to: constr(regex=r"^[0-9a-z]{40}$") = Query(..., alias="crossMemberAddressTo"),
    type: conint(ge=0, le=2) = ...,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCrossTransactionCrossRouteView:
    """
    getBestCrossRoute_1
    """
    return create_factory_class(ResponseResultCrossTransactionCrossRouteView).build()


@app.post(
    "/manage/cross-transaction/cross/transfer",
    response_model=ResponseResultCrossTransactionView,
)
def cross_transfer_1(
    body: CrossTransferRequest,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
    content__type: Optional[ContentType5] = Header(None, alias="Content-Type"),
) -> ResponseResultCrossTransactionView:
    """
    crossTransfer_1
    """
    return create_factory_class(ResponseResultCrossTransactionView).build()


@app.get(
    "/manage/cross-transaction/cross/{id}",
    response_model=ResponseResultCrossTransactionView,
    responses={"404": {"model": ResponseResultCrossTransactionView}},
)
def get_by_id(id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")) -> ResponseResultCrossTransactionView:
    """
    getById
    """
    return create_factory_class(ResponseResultCrossTransactionView).build()


@app.post(
    "/manage/cross-transaction/cross/{id}/complete",
    response_model=ResponseResultBlockchainTransactionResponse,
)
def complete(
    id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")
) -> ResponseResultBlockchainTransactionResponse:
    """
    complete
    """
    return create_factory_class(ResponseResultBlockchainTransactionResponse).build()


@app.post(
    "/manage/cross-transaction/cross/{id}/decode",
    response_model=ResponseResultCrossTransactionView,
)
def decode_payload(
    id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")
) -> ResponseResultCrossTransactionView:
    """
    decodePayload
    """
    return create_factory_class(ResponseResultCrossTransactionView).build()


@app.get(
    "/manage/cross-transaction/cross/{id}/details",
    response_model=ResponseResultCrossTransactionDetailsView,
    responses={"404": {"model": ResponseResultCrossTransactionDetailsView}},
)
def get_details_by_id(
    id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")
) -> ResponseResultCrossTransactionDetailsView:
    """
    getDetailsById
    """
    return create_factory_class(ResponseResultCrossTransactionDetailsView).build()


@app.post(
    "/manage/cross-transaction/cross/{id}/withdraw",
    response_model=ResponseResultBoolean,
)
def withdraw(id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")) -> ResponseResultBoolean:
    """
    withdraw
    """
    pass


@app.post(
    "/manage/cross-transaction/cross/{id}/withdraw/{withdraw_id}/confirm",
    response_model=ResponseResultBlockchainTransactionResponse,
)
def confirm_withdraw(
    id: UUID,
    withdraw_id: UUID = Path(..., alias="withdrawId"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultBlockchainTransactionResponse:
    """
    confirmWithdraw
    """
    pass


@app.post(
    "/manage/cross-transaction/cross/{id}/withdraw/{withdraw_id}/reject",
    response_model=ResponseResultBlockchainTransactionResponse,
)
def reject_withdraw(
    id: UUID,
    withdraw_id: UUID = Path(..., alias="withdrawId"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultBlockchainTransactionResponse:
    """
    rejectWithdraw
    """
    pass


@app.get(
    "/manage/cross-transaction/exchange",
    response_model=ResponseResultPagingResultExchangeTransactionView,
)
def get_page(
    status: Optional[conint(ge=0, le=2)] = None,
    page_index: conint(ge=0) = Query(..., alias="pageIndex"),
    page_size: Optional[conint(ge=1)] = Query(20, alias="pageSize"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultPagingResultExchangeTransactionView:
    """
    getPage
    """
    pass


@app.post(
    "/manage/cross-transaction/exchange/transfer",
    response_model=ResponseResultExchangeTransactionView,
)
def exchange_transfer_1(
    body: ExchangeTransferRequest,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
    content__type: Optional[ContentType8] = Header(None, alias="Content-Type"),
) -> ResponseResultExchangeTransactionView:
    """
    exchangeTransfer_1
    """
    pass


@app.get(
    "/manage/cross-transaction/public/cross/customer/routes",
    response_model=ResponseResultCrossTransactionCrossRoutesView,
    responses={"404": {"model": ResponseResultCrossTransactionCrossRoutesView}},
)
def get_best_cross_routes_by_customer(
    amount: confloat(ge=0.0),
    currency_code_from: conint(ge=0, le=999) = Query(..., alias="currencyCodeFrom"),
    currency_code_to: conint(ge=0, le=999) = Query(..., alias="currencyCodeTo"),
    type: conint(ge=0, le=2) = ...,
    country_code: Optional[constr(min_length=3, max_length=3)] = Query(None, alias="countryCode"),
    customer_identifier: constr(regex=r"^[0-9a-z]{64}$") = Query(..., alias="customerIdentifier"),
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCrossTransactionCrossRoutesView:
    """
    getBestCrossRoutesByCustomer
    """
    pass


@app.get(
    "/manage/cross-transaction/public/cross/route/{id}",
    response_model=ResponseResultRoutingView,
    responses={"404": {"model": ResponseResultRoutingView}},
)
def get_route_by_id_1(id: int, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")) -> ResponseResultRoutingView:
    """
    getRouteById_1
    """
    pass


@app.post(
    "/manage/cross-transaction/public/cross/transfer",
    response_model=ResponseResultCrossTransactionView,
)
def cross_transfer(
    body: CrossTransferPublicRequest,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
    content__type: Optional[ContentType14] = Header(None, alias="Content-Type"),
) -> ResponseResultCrossTransactionView:
    """
    crossTransfer
    """
    pass


@app.get(
    "/manage/cross-transaction/public/cross/transfer/route",
    response_model=ResponseResultCrossTransactionCrossRouteView,
    responses={"404": {"model": ResponseResultCrossTransactionCrossRouteView}},
)
def get_best_cross_route(
    amount: confloat(ge=0.0),
    currency_code_from: conint(ge=0, le=999) = Query(..., alias="currencyCodeFrom"),
    currency_code_to: conint(ge=0, le=999) = Query(..., alias="currencyCodeTo"),
    cross_member_address_from: str = Query(..., alias="crossMemberAddressFrom"),
    cross_member_address_to: constr(regex=r"^[0-9a-z]{40}$") = Query(..., alias="crossMemberAddressTo"),
    type: conint(ge=0, le=2) = ...,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCrossTransactionCrossRouteView:
    """
    getBestCrossRoute
    """
    pass


@app.get(
    "/manage/cross-transaction/public/cross/{id}",
    response_model=ResponseResultCrossTransactionView,
    responses={"404": {"model": ResponseResultCrossTransactionView}},
)
def get_transaction_by_id(
    id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")
) -> ResponseResultCrossTransactionView:
    """
    getTransactionById
    """
    pass


@app.get(
    "/manage/cross-transaction/public/exchange/route",
    response_model=ResponseResultCrossTransactionExchangeRouteView,
    responses={"404": {"model": ResponseResultCrossTransactionExchangeRouteView}},
)
def get_best_exchange_route(
    amount: confloat(ge=0.0),
    currency_code_from: conint(ge=0, le=999) = Query(..., alias="currencyCodeFrom"),
    currency_code_to: conint(ge=0, le=999) = Query(..., alias="currencyCodeTo"),
    type: conint(ge=0, le=2) = ...,
    f_p_s_i_d: Optional[str] = Header(None, alias="FPSID"),
) -> ResponseResultCrossTransactionExchangeRouteView:
    """
    getBestExchangeRoute
    """
    pass


@app.get(
    "/manage/cross-transaction/public/exchange/route/{id}",
    response_model=ResponseResultRoutingView,
    responses={"404": {"model": ResponseResultRoutingView}},
)
def get_route_by_id(id: int, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")) -> ResponseResultRoutingView:
    """
    getRouteById
    """
    pass


@app.get(
    "/manage/cross-transaction/public/exchange/{id}",
    response_model=ResponseResultExchangeTransactionView,
    responses={"404": {"model": ResponseResultExchangeTransactionView}},
)
def get_public_by_id(
    id: UUID, f_p_s_i_d: Optional[str] = Header(None, alias="FPSID")
) -> ResponseResultExchangeTransactionView:
    """
    getPublicById
    """
    pass
