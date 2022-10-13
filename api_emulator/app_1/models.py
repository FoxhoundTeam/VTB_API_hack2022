from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, conint, constr


class Error(BaseModel):
    errorCode: Optional[constr(max_length=5)] = Field(None, description="Код ошибки")
    errorMessage: Optional[constr(max_length=1000)] = Field(None, description="Краткое описание ошибки")


class OpenApiLeadImpersonalRequestDto(BaseModel):
    sourceLeadId: constr(max_length=128) = Field(
        ...,
        description="Идентификатор лида в системе источнике используется для предотвращения повторного добавления одного и того же лида в ПКБ.",
        example="ap123",
        title="Идентификатор лида в источнике",
    )
    phone: constr(max_length=20) = Field(
        ...,
        description="Номер телефона контакта юридического лица. Атрибут является обязательным для заполнения.  Длина составляет не менее 10 и не более 20 знаков. В обработку принимаются только цифры {0..9}, прочие символы отбрасываются. Если первая цифра 7 или 8, то она отбрасывается.",
        example=7123456789,
        title="Телефон",
    )
    inn: Optional[constr(max_length=12)] = Field(
        None,
        description="Строка длинной 10 или 12 символов.",
        example="547779835982",
        title="ИНН",
    )
    companyName: Optional[constr(max_length=255)] = Field(
        None,
        description="Название юридического лица.",
        example="ИП Иванов Иван Иванович",
        title="Компания",
    )
    city: Optional[constr(max_length=100)] = Field(
        None,
        description="Город для определения точки продаж из справочника ПКБ.",
        example="Москва",
        title="Город",
    )
    creationComment: Optional[constr(max_length=255)] = Field(
        None,
        description="Комментарий при создании лида.",
        example="Перспективный клиент",
        title="Комментарий",
    )
    productCode: Optional[constr(max_length=150)] = Field(
        None,
        description="Код интересующего продукта ВТБ.",
        example="Payments",
        title="Код продукта",
    )
    servicePackageCode: Optional[constr(max_length=255)] = Field(
        None, description="Код тарифа", example="Start", title="Код тарифа"
    )
    utmSource: Optional[constr(max_length=255)] = Field(
        None,
        description="Наименование источника кампании.",
        example="Yandex",
        title="Источник кампании",
    )
    utmCampaign: Optional[constr(max_length=255)] = Field(
        None,
        description="Наименование кампании.",
        example="Cifra",
        title="Название кампании",
    )


class ResponseCode(Enum):
    SUCCESS = "SUCCESS"
    NO_LEADS = "NO_LEADS"
    INVALID_PHONE = "INVALID_PHONE"
    INVALID_PRODUCT = "INVALID_PRODUCT"
    INVALID_SERVICE_PACKAGE = "INVALID_SERVICE_PACKAGE"
    UNEXPECTED_ERROR = "UNEXPECTED_ERROR"
    LEAD_ALREADY_EXISTS = "LEAD_ALREADY_EXISTS"
    INVALID_SOURCE_LEAD_ID = "INVALID_SOURCE_LEAD_ID"
    NO_PERMISSIONS = "NO_PERMISSIONS"
    AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"
    UNDEFINED = "UNDEFINED"


class OpenApiLeadImpersonalResponseDto(BaseModel):
    sourceLeadId: Optional[constr(max_length=128)] = Field(
        None,
        description="Идентификатор лида в системе источнике используется для предотвращения повторного добавления одного и того же лида в ПКБ.",
        example="ap123",
        title="Идентификатор лида в источнике",
    )
    leadId: Optional[conint(ge=0, le=9007199254740991)] = Field(
        None,
        description="Идентификатор лида в ПКБ.",
        example=456789,
        title="Идентфикатор лида",
    )
    status: Optional[constr(max_length=128)] = Field(
        None,
        description="'Код публичного статуса лида. New - новый, VerificationFailed - не пройдена проверка, Duple - дубль, Processing - в работе, ProductOpened - продукт оформлен, CallFailed - окончательный недозвон, Rejected - закрыт отказом, TimeOut - закрыт по истечению срока.''",
        example="New",
        title="Статус",
    )
    responseCode: Optional[ResponseCode] = Field(
        None,
        description="Код ответа. SUCCESS - успешно, NO_LEADS - в запросе отсутствуют лиды, INVALID_PHONE - в запросе отсутствует или некорректный телефон, UNEXPECTED_ERROR - неизвестная ошибка на сервере, LEAD_ALREADY_EXISTS - лид с таким идентификатором в источнике уже существует, INVALID_SOURCE_LEAD_ID - в запросе отсутствует идентификатор лида в источнике. INVALID_PRODUCT - некорректный продукт, INVALID_SERVICE_PACKAGE - некорректный пакет услуг продукта, AUTHENTICATION_FAILED - не пройдена аутентификация, UNDEFINED - запрос вернул неизвестный результат",
        example="SUCCESS",
        title="Код ответа",
    )
    responseCodeDescription: Optional[constr(max_length=255)] = Field(
        None,
        description="Расшифровка ответа и предупреждения.",
        example="Операция выполнена успешно.",
        title="Описание ответа",
    )


class ResponseCode1(Enum):
    SUCCESS = "SUCCESS"
    LEAD_NOT_FOUND = "LEAD_NOT_FOUND"
    UNEXPECTED_ERROR = "UNEXPECTED_ERROR"
    NO_PERMISSIONS = "NO_PERMISSIONS"
    AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"


class OpenApiLeadStatusResponseDto(BaseModel):
    leadId: Optional[conint(ge=0, le=9007199254740991)] = Field(
        None,
        description="Идентификатор лида в ПКБ.",
        example=456789,
        title="Идентфикатор лида",
    )
    sourceLeadId: Optional[constr(max_length=128)] = Field(
        None,
        description="Идентификатор лида в системе источнике используется для предотвращения повторного добавления одного и того же лида в ПКБ.",
        example="ap123",
        title="Идентификатор лида в источнике",
    )
    status: Optional[constr(max_length=128)] = Field(
        None,
        description="Код публичного статуса лида. New - новый, VerificationFailed - не пройдена проверка, Duple - дубль, Processing - в работе, ProductOpened - продукт оформлен, CallFailed - окончательный недозвон, Rejected - закрыт отказом, TimeOut - закрыт по истечению срока.",
        example="Processing",
        title="Статус",
    )
    statusChanged: Optional[datetime] = Field(
        None,
        description="Дата и время изменения статуса",
        example="2020-11-02T14:32:36.12Z",
        title="Дата изменения статуса",
    )
    responseCode: Optional[ResponseCode1] = Field(
        None,
        description="'Код ответа. SUCCESS - успешно, LEAD_NOT_FOUND - лид не найден,\n"
        " UNEXPECTED_ERROR - неизвестная ошибка на сервере, NO_PERMISSIONS - отсутствует доступ к указанному лиду, AUTHENTICATION_FAILED - не пройдена аутентификация'",
        example="Success",
        title="Код ответа",
    )
    responseCodeDescription: Optional[constr(max_length=255)] = Field(
        None,
        description="Расшифровка ответа и предупреждения.",
        example="Операция выполнена успешно.",
        title="Описание ответа",
    )


class OpenApiLeadCheckRequestDto(BaseModel):
    inn: constr(max_length=12) = Field(
        ...,
        description="Строка длинной 10 или 12 символов.",
        example="547779835982",
        title="ИНН",
    )
    productCode: constr(max_length=150) = Field(
        ...,
        description="Код интересующего продукта ВТБ.",
        example="Payments",
        title="Код продукта",
    )


class ResponseCode2(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NO_LEADS = "NO_LEADS"
    INVALID_INN = "INVALID_INN"
    INVALID_PRODUCT = "INVALID_PRODUCT"
    NO_PERMISSIONS = "NO_PERMISSIONS"
    AUTHENTICATION_FAILED = "AUTHENTICATION_FAILED"
    UNEXPECTED_ERROR = "UNEXPECTED_ERROR"


class OpenApiLeadCheckResponseDto(BaseModel):
    responseCode: ResponseCode2 = Field(
        ...,
        description="'Код ответа. POSITIVE - Лид может быть взят в работу,\n"
        "NEGATIVE - Лид не будет взят в работу,\n"
        "NO_LEADS - в запросе отсутствуют лиды,\n"
        "INVALID_INN - ИНН имеет неверный формат,\n"
        "INVALID_PRODUCT - указанный продукт не существует,\n"
        "NO_PERMISSION - доступ к данному методу запрещен,\n"
        "UNEXPECTED_ERROR - при обработке запроса произошла неизвестная ошибка, обратитесь в поддержку,\n"
        "AUTHENTICATION_FAILED - не пройдена аутентификация'",
        example="POSITIVE",
        title="Код ответа",
    )
    responseCodeDescription: Optional[constr(max_length=255)] = Field(
        None,
        description="Расшифровка ответа и предупреждения.",
        example="Операция выполнена успешно.",
        title="Описание ответа",
    )


class OpenApiLeadsImpersonalRequestDto(BaseModel):
    leads: List[OpenApiLeadImpersonalRequestDto] = Field(..., description="Запрос на создание лида", max_items=255)


class OpenApiLeadsImpersonalResponseDto(BaseModel):
    leads: List[OpenApiLeadImpersonalResponseDto] = Field(..., description="Ответ на создание лида", max_items=255)


class OpenApiLeadsStatusResponseDto(BaseModel):
    leads: List[OpenApiLeadStatusResponseDto] = Field(..., description="Ответ на запрос статуса лида", max_items=255)


class OpenApiLeadsCheckRequestDto(BaseModel):
    leads: List[OpenApiLeadCheckRequestDto] = Field(..., description="Запросы на проверку лидов", max_items=255)


class OpenApiLeadsCheckResponseDto(BaseModel):
    leads: List[OpenApiLeadCheckResponseDto] = Field(..., description="Ответы по проверке лидов", max_items=255)
