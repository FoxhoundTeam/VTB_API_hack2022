from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ApplicationStatus(Enum):
    prescore_approved = "prescore_approved"
    prescore_denied = "prescore_denied"
    processing = "processing"


class CarloanResponseDecision(BaseModel):
    application_status: ApplicationStatus
    comment: Optional[str] = Field("Комментарий", description="Комментарий к решению", title="Comment")
    decision_date: Optional[date] = Field(None, description="Дата решения", title="Decision Date")
    decision_end_date: Optional[date] = Field(
        None, description="Дата окончания действия решения", title="Decision End Date"
    )
    monthly_payment: Optional[float] = Field(
        None, description="Максимальный ежемесячный платёж", title="Monthly Payment"
    )


class Gender(Enum):
    male = "male"
    female = "female"
    unknown = "unknown"


class Person(BaseModel):
    birth_date_time: Optional[date] = Field(None, description="Дата рождения", title="Birth Date Time")
    birth_place: Optional[str] = Field("Воронеж", description="Место рождения", title="Birth Place")
    family_name: Optional[str] = Field("Передачкин", description="Фамилия", title="Family Name")
    first_name: Optional[str] = Field("Алексей", description="Имя", title="First Name")
    gender: Optional[Gender] = None
    middle_name: Optional[str] = Field("Петрович", description="Отчество", title="Middle Name")
    nationality_country_code: Optional[str] = Field(
        "RU", description="Национальность", title="Nationality Country Code"
    )


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class CarloanResponseApplication(BaseModel):
    VTB_client_ID: Optional[int] = Field(None, description="Идентификатор клиента", title="Vtb Client Id")
    decision_report: CarloanResponseDecision


class CustomerParty(BaseModel):
    email: Optional[str] = Field("apetrovich@example.com", description="Email", title="Email")
    income_amount: Optional[int] = Field(None, description="Доход клиента, руб", title="Income Amount")
    person: Person
    phone: Optional[str] = Field(79156670849, description="Мобильный телефон", title="Phone")


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")


class Carloan(BaseModel):
    comment: Optional[str] = Field("Комментарий", description="Комментарий", title="Comment")
    customer_party: CustomerParty
    _datetime: Optional[datetime] = Field(None, description="Дата/время запроса", title="Datetime", alias="datetime")
    interest_rate: Optional[float] = Field(None, description="Процентная ставка", title="Interest Rate")
    requested_amount: Optional[int] = Field(None, description="Сумма кредита, руб", title="Requested Amount")
    requested_term: Optional[int] = Field(None, description="Срок кредита, лет", title="Requested Term")
    trade_mark: Optional[str] = Field("Nissan", description="Марка автомобиля", title="Trade Mark")
    vehicle_cost: Optional[int] = Field(None, description="Стоимость автомобиля", title="Vehicle Cost")


class CarloanResponse(BaseModel):
    application: CarloanResponseApplication
    _datetime: Optional[datetime] = Field(None, description="Дата", title="Datetime", alias="datetime")
