# generated by fastapi-codegen:
#   filename:  new_yamls/app_3.yaml
#   timestamp: 2022-10-11T21:09:52+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, confloat, conint, constr


class CcSignDto(BaseModel):
    r: constr(regex=r"^[0-9a-z]{62}||[0-9a-z]{64}$") = Field(..., description="Point R")
    s: constr(regex=r"^[0-9a-z]{62}||[0-9a-z]{64}$") = Field(..., description="Point S")
    v: conint(ge=27, le=28) = Field(..., description="Recover Id")


class CrossTransactionBestRoutingItemRequest(BaseModel):
    id: Optional[conint(ge=0)] = Field(None, description="Идентификатор контракта")
    requestId: constr(regex=r"\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b") = Field(
        ..., description="Идентификатор запроса"
    )


class ExchangeTransferPublicRequest(BaseModel):
    route: CrossTransactionBestRoutingItemRequest
    addressFrom: constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$") = Field(..., description="Адрес отправителя")
    senderSummaryAmount: float = Field(..., description="Сумма к отправке")
    receiverSummaryAmount: float = Field(..., description="Сумма к получению")
    to: Optional[constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$")] = Field(None, description="Адрес аккаунта")
    currencyCodeFrom: conint(ge=1, le=999) = Field(..., description="Код продаваемой валюты")
    currencyCodeTo: conint(ge=1, le=999) = Field(..., description="Код покупаемой валюты")
    payload: Optional[constr(min_length=0, max_length=4028)] = Field(None, description="Дополнительная информация")
    invoiceNumber: Optional[constr(min_length=0, max_length=100)] = Field(None, description="Номер счета")
    sig: CcSignDto
    type: conint(ge=0, le=2) = Field(..., description="Направление маршрута")
    iat: int = Field(..., description="Время создания, в миллисекундах")
    exp: int = Field(..., description="Истекшее время объекта, в миллисекундах")


class ExchangeTransactionView(BaseModel):
    id: Optional[UUID] = Field(None, description="Идентификатор перевода")
    addressFrom: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Адрес отправителя")
    amountInput: Optional[float] = Field(None, description="Сумма отправителя (в валюте отправителя)")
    amountOutput: Optional[float] = Field(None, description="Сумма перевода")
    addressTo: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Адрес получателя")
    currencyCodeFrom: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты отправления перевода")
    currencyCodeTo: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты получения перевода")
    transactionId: Optional[constr(regex=r"^[0-9a-z]{64}$")] = Field(None, description="Идентификатор транзакции в БЧ")
    state: Optional[conint(ge=0, le=7)] = Field(None, description="Статус выполнения перевода")
    invoiceNumber: Optional[constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$")] = Field(None, description="Номер счета")
    errorCode: Optional[conint(ge=0)] = Field(None, description="Код ошибки")
    errorData: Optional[constr(min_length=0, max_length=2048)] = Field(None, description="Дополнительные данные ошибки")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    updatedAt: Optional[datetime] = Field(None, description="Дата последнего обновления")


class ResponseResultExchangeTransactionView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[ExchangeTransactionView] = None


class AccountSecretKey(BaseModel):
    publicKeyTo: str = Field(..., description="Публичный ключ аккаунта на который производится перевод")
    encryptedSecretKey: str = Field(..., description="Зашифрованный секретный ключ")


class EncryptedPayload(BaseModel):
    secretKeys: List[AccountSecretKey] = Field(..., description="Секретные ключи")
    payload: constr(min_length=0, max_length=4028) = Field(..., description="Сообщение")


class CrossTransactionView(BaseModel):
    id: Optional[UUID] = Field(None, description="Идентификатор транзакции текущей платформы")
    addressFrom: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Адрес отправителя")
    amountInput: Optional[float] = Field(None, description="Сумма отправителя (в валюте отправителя)")
    amountOutput: Optional[float] = Field(None, description="Сумма перевода")
    addressTo: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Адрес получателя")
    currencyCodeFrom: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты отправления перевода")
    currencyCodeTo: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты получения перевода")
    customerIdentifier: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Идентификатор получателя перевода"
    )
    customerBankProduct: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Банковский продукт получателя"
    )
    purposeOfPayment: Optional[constr(min_length=0, max_length=255)] = Field(None, description="Назначение платежа")
    transactionId: Optional[constr(regex=r"^[0-9a-z]{64}$")] = Field(None, description="Идентификатор транзакции в БЧ")
    state: Optional[conint(ge=0, le=7)] = Field(None, description="Статус выполнения перевода")
    errorCode: Optional[conint(ge=0)] = Field(None, description="Код ошибки")
    errorData: Optional[constr(min_length=0, max_length=2048)] = Field(None, description="Дополнительные данные ошибки")
    payloadEncrypted: Optional[bool] = Field(None, description="Признак зашифрованный payload или нет")
    externalSystemId: Optional[str] = Field(None, description="Идентификатор внешней системы")
    externalTransactionId: Optional[str] = Field(None, description="Идентификатор транзакции внешней системы")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    updatedAt: Optional[datetime] = Field(None, description="Дата последнего обновления")
    outbound: Optional[bool] = None
    inbound: Optional[bool] = None


class ResponseResultCrossTransactionView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[CrossTransactionView] = None


class ExchangeTransferRequest(BaseModel):
    route: CrossTransactionBestRoutingItemRequest
    addressFrom: constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$") = Field(..., description="Адрес отправителя")
    senderSummaryAmount: float = Field(..., description="Сумма к отправке")
    receiverSummaryAmount: float = Field(..., description="Сумма к получению")
    to: Optional[constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$")] = Field(None, description="Адрес аккаунта")
    currencyCodeFrom: conint(ge=1, le=999) = Field(..., description="Код продаваемой валюты")
    currencyCodeTo: conint(ge=1, le=999) = Field(..., description="Код покупаемой валюты")
    payload: Optional[constr(min_length=0, max_length=4028)] = Field(None, description="Дополнительная информация")
    invoiceNumber: Optional[constr(min_length=0, max_length=100)] = Field(None, description="Номер счета")
    type: conint(ge=0, le=2) = Field(..., description="Направление маршрута")


class ResponseResultBoolean(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[bool] = None


class BlockchainTransactionResponse(BaseModel):
    txId: Optional[constr(regex=r"^[0-9a-z]{64}$")] = Field(None, description="Идентификатор транзакции в HLF")
    result: Optional[str] = Field(None, description="Результат выполнения")


class ResponseResultBlockchainTransactionResponse(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[BlockchainTransactionResponse] = None


class CrossTransferRequest(BaseModel):
    route: CrossTransactionBestRoutingItemRequest
    addressFrom: str = Field(..., description="Адрес отправителя")
    receiverSummaryAmount: float = Field(..., description="Сумма к получению")
    senderSummaryAmount: float = Field(..., description="Сумма к отправке")
    crossMemberAddressTo: Optional[constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$")] = Field(
        None, description="Адрес аккаунта участника ТГП получателя"
    )
    currencyCodeFrom: conint(ge=1, le=999) = Field(..., description="Код продаваемой валюты")
    currencyCodeTo: conint(ge=1, le=999) = Field(..., description="Код покупаемой валюты")
    payload: Optional[constr(min_length=0, max_length=4028)] = Field(None, description="Дополнительная информация")
    customerIdentifier: constr(min_length=0, max_length=255) = Field(..., description="Идентификатор получателя")
    customerBankProduct: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Банковский продукт получателя"
    )
    purposeOfPayment: Optional[constr(min_length=0, max_length=255)] = Field(None, description="Назначение платежа")
    type: conint(ge=0, le=2) = Field(..., description="Направление маршрута")
    externalSystemId: Optional[str] = Field(None, description="Идентификатор внешней системы")
    externalTransactionId: Optional[str] = Field(None, description="Идентификатор транзакции внешней системы")


class CrossTransactionExchangeRouteView(BaseModel):
    senderSummaryAmount: Optional[float] = Field(None, description="Сумма к отправке")
    receiverSummaryAmount: Optional[float] = Field(None, description="Сумма к получению")
    routeId: Optional[conint(ge=1)] = Field(None, description="Идентификатор маршрута на платформе")
    requestId: Optional[constr(regex=r"\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b")] = Field(
        None, description="Идентификатор запроса"
    )
    type: Optional[conint(ge=0, le=2)] = Field(None, description="Направление маршрута")


class ResponseResultCrossTransactionExchangeRouteView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[CrossTransactionExchangeRouteView] = None


class RoutingView(BaseModel):
    id: Optional[conint(ge=1)] = Field(None, description="Идентификатор маршрута")
    routeJson: Optional[constr(min_length=0, max_length=3072)] = Field(None, description="Маршрут")


class CrossTransactionCrossRouteView(BaseModel):
    currencyCodeTo: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты получателя")
    currencyCodeFrom: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты отправителя")
    outgoingCommissionAmount: Optional[confloat(ge=0.0)] = Field(None, description="Кол-во исходящей комиссии")
    incomingCommissionAmount: Optional[confloat(ge=0.0)] = Field(None, description="Кол-во входящей комиссии")
    senderSummaryAmount: Optional[float] = Field(None, description="Сумма к отправке")
    receiverSummaryAmount: Optional[float] = Field(None, description="Сумма к получению")
    receiverPublicKeys: Optional[List[str]] = Field(
        None,
        description="Публичные ключи получателей payload",
        max_items=2147483647,
        min_items=1,
    )
    requestId: Optional[constr(regex=r"\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b")] = Field(
        None, description="Идентификатор запроса"
    )
    routeId: Optional[conint(ge=1)] = Field(None, description="Идентификатор маршрута на платформе")
    type: Optional[conint(ge=0, le=2)] = Field(None, description="Направление маршрута")


class ResponseResultCrossTransactionCrossRouteView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[CrossTransactionCrossRouteView] = None


class CrossTransactionCrossRouteItem(BaseModel):
    route: Optional[CrossTransactionCrossRouteView] = None
    crossMemberTo: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Участник получатель ТГП")
    crossMemberNameTo: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(
        None, description="Наименование участника получатель ТГП"
    )
    crossCustomerName: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Наименование участника получателя ТГП"
    )
    errorMessage: Optional[constr(min_length=0, max_length=2048)] = Field(None, description="Сообщение об ошибке")


class CrossTransactionCrossRoutesView(BaseModel):
    routes: Optional[List[CrossTransactionCrossRouteItem]] = Field(
        None,
        description="Трансграничные маршруты для клиента",
        max_items=2147483647,
        min_items=0,
    )


class ResponseResultCrossTransactionCrossRoutesView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[CrossTransactionCrossRoutesView] = None


class QueryResponseMetadata(BaseModel):
    fetchedRecordsCount: Optional[int] = Field(None, description="Количество полученных данных")
    bookmark: Optional[str] = Field(None, description="Закладка для получения следующей страницы")


class PagingResultCrossTransactionView(BaseModel):
    metadata: Optional[QueryResponseMetadata] = None
    items: Optional[List[CrossTransactionView]] = Field(None, description="Список элементов")


class ResponseResultPagingResultCrossTransactionView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[PagingResultCrossTransactionView] = None


class CrossTransactionWithdrawalView(BaseModel):
    id: Optional[UUID] = Field(None, description="Идентификатор транзакции")
    txId: Optional[constr(regex=r"^[0-9a-z]{64}$")] = Field(None, description="Идентификатор транзакции из блокчейна")
    state: Optional[conint(ge=0, le=6)] = Field(None, description="Статус")
    errorCode: Optional[conint(ge=0)] = Field(None, description="Код ошибки")
    errorData: Optional[constr(min_length=0, max_length=2048)] = Field(None, description="Дополнительные данные ошибки")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    updatedAt: Optional[datetime] = Field(None, description="Дата последнего обновления")


class CountryView(BaseModel):
    code: Optional[conint(le=999)] = Field(None, description="Код страны")
    alpha2: Optional[constr(min_length=2, max_length=2)] = Field(None, description="Alpha 2 страны")
    alpha3: Optional[constr(min_length=3, max_length=3)] = Field(None, description="Alpha 3 страны")
    title: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Наименование страны в требуемой локализации"
    )


class PagingResultCountryView(BaseModel):
    metadata: Optional[QueryResponseMetadata] = None
    items: Optional[List[CountryView]] = Field(None, description="Список элементов")


class ResponseResultPagingResultCountryView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[PagingResultCountryView] = None


class ResponseResultCountryView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[CountryView] = None


class ResponseResultListCountryView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[List[CountryView]] = None


class AuthRequest(BaseModel):
    username: Optional[constr(min_length=0, max_length=20)] = Field(None, description="Логин")
    password: Optional[constr(min_length=0, max_length=20)] = Field(None, description="Пароль")
    grant_type: Optional[constr(min_length=0, max_length=20)] = Field(None, description="grant_type")
    client_id: Optional[constr(min_length=0, max_length=20)] = Field(None, description="client_id")
    client_secret: Optional[constr(min_length=0, max_length=20)] = Field(None, description="client_type")


class AuthResponse(BaseModel):
    access_token: Optional[str] = Field(None, description="Токен")


class Language(Enum):
    UNDEFINED = "UNDEFINED"
    DE = "DE"
    EN = "EN"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    NL = "NL"
    RU = "RU"


class ContentType(Enum):
    application_x_www_form_urlencoded = "application/x-www-form-urlencoded"


class AuthOauthTokenPostRequest(BaseModel):
    username: Optional[constr(min_length=0, max_length=20)] = Field(None, description="Логин")
    password: Optional[constr(min_length=0, max_length=20)] = Field(None, description="Пароль")
    grant_type: Optional[constr(min_length=0, max_length=20)] = Field(None, description="grant_type")
    client_id: Optional[constr(min_length=0, max_length=20)] = Field(None, description="client_id")
    client_secret: Optional[constr(min_length=0, max_length=20)] = Field(None, description="client_type")


class ContentType1(Enum):
    application_x_www_form_urlencoded = "application/x-www-form-urlencoded"


class ContentType2(Enum):
    application_x_www_form_urlencoded = "application/x-www-form-urlencoded"


class ContentType3(Enum):
    application_json = "application/json"


class ContentType4(Enum):
    application_json = "application/json"


class ContentType5(Enum):
    application_json = "application/json"


class ContentType6(Enum):
    application_json = "application/json"


class ContentType7(Enum):
    application_json = "application/json"


class ContentType8(Enum):
    application_json = "application/json"


class Language1(Enum):
    UNDEFINED = "UNDEFINED"
    DE = "DE"
    EN = "EN"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    NL = "NL"
    RU = "RU"


class Language2(Enum):
    UNDEFINED = "UNDEFINED"
    DE = "DE"
    EN = "EN"
    ES = "ES"
    FR = "FR"
    IT = "IT"
    NL = "NL"
    RU = "RU"


class ContentType9(Enum):
    application_json = "application/json"


class ContentType10(Enum):
    application_json = "application/json"


class ContentType11(Enum):
    application_json = "application/json"


class ContentType12(Enum):
    application_json = "application/json"


class ContentType13(Enum):
    application_json = "application/json"


class ContentType14(Enum):
    application_json = "application/json"


class CrossTransferPublicRequest(BaseModel):
    id: UUID = Field(..., description="Идентификатор перевода")
    route: CrossTransactionBestRoutingItemRequest
    addressFrom: constr(regex=r"^[0-9a-z]{40}$") = Field(..., description="Адрес отправителя")
    receiverSummaryAmount: float = Field(..., description="Сумма к получению")
    senderSummaryAmount: float = Field(..., description="Сумма к отправке")
    crossMemberAddressFrom: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(
        None, description="Адрес аккаунта участника ТГП отправителя"
    )
    crossMemberAddressTo: Optional[constr(regex=r"^[0-9a-z]{40}$|^[0-9a-z]{64}$")] = Field(
        None, description="Адрес аккаунта участника ТГП получателя"
    )
    currencyCodeFrom: conint(ge=1, le=999) = Field(..., description="Код продаваемой валюты")
    currencyCodeTo: conint(ge=1, le=999) = Field(..., description="Код покупаемой валюты")
    encryptedPayload: EncryptedPayload
    sig: CcSignDto
    iat: int = Field(..., description="Время создания, в миллисекундах")
    exp: int = Field(..., description="Истекшее время объекта, в миллисекундах")
    type: conint(ge=0, le=2) = Field(..., description="Направление маршрута")
    externalSystemId: Optional[str] = Field(None, description="Идентификатор внешней системы")
    externalTransactionId: Optional[str] = Field(None, description="Идентификатор транзакции внешней системы")


class ResponseResultRoutingView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[RoutingView] = None


class PagingResultExchangeTransactionView(BaseModel):
    metadata: Optional[QueryResponseMetadata] = None
    items: Optional[List[ExchangeTransactionView]] = Field(None, description="Список элементов")


class ResponseResultPagingResultExchangeTransactionView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[PagingResultExchangeTransactionView] = None


class CrossTransactionDetailsView(BaseModel):
    id: Optional[UUID] = Field(None, description="Идентификатор транзакции текущей платформы")
    addressFrom: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Адрес отправителя")
    amountInput: Optional[float] = Field(None, description="Сумма отправителя (в валюте отправителя)")
    amountOutput: Optional[float] = Field(None, description="Сумма перевода")
    addressTo: Optional[constr(regex=r"^[0-9a-z]{40}$")] = Field(None, description="Адрес получателя")
    currencyCodeFrom: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты отправления перевода")
    currencyCodeTo: Optional[conint(ge=0, le=999)] = Field(None, description="Код валюты получения перевода")
    customerIdentifier: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Идентификатор получателя перевода"
    )
    customerBankProduct: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Банковский продукт получателя"
    )
    purposeOfPayment: Optional[constr(min_length=0, max_length=255)] = Field(None, description="Назначение платежа")
    transactionId: Optional[constr(regex=r"^[0-9a-z]{64}$")] = Field(None, description="Идентификатор транзакции в БЧ")
    state: Optional[conint(ge=0, le=7)] = Field(None, description="Статус выполнения перевода")
    errorCode: Optional[conint(ge=0)] = Field(None, description="Код ошибки")
    errorData: Optional[constr(min_length=0, max_length=2048)] = Field(None, description="Дополнительные данные ошибки")
    payloadEncrypted: Optional[bool] = Field(None, description="Признак зашифрованный payload или нет")
    externalSystemId: Optional[str] = Field(None, description="Идентификатор внешней системы")
    externalTransactionId: Optional[str] = Field(None, description="Идентификатор транзакции внешней системы")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    updatedAt: Optional[datetime] = Field(None, description="Дата последнего обновления")
    routeJson: Optional[constr(min_length=0, max_length=3072)] = Field(
        None, description="Маршрут транзакций в формате json"
    )
    withdrawals: Optional[List[CrossTransactionWithdrawalView]] = Field(
        None,
        description="Список попыток списания средств",
        max_items=2147483647,
        min_items=0,
    )
    outbound: Optional[bool] = None
    inbound: Optional[bool] = None


class ResponseResultCrossTransactionDetailsView(BaseModel):
    timestamp: Optional[datetime] = None
    message: Optional[str] = None
    data: Optional[CrossTransactionDetailsView] = None