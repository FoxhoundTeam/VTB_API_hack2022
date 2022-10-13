from typing import Optional, Union

from fastapi import FastAPI, Header, Query
from pydantic import conint, constr

from common.factories import create_factory_class

from .models import (
    XCLIENTCHANNEL2,
    XCLIENTCHANNEL5,
    GenericError,
    PageDtoRsCategoryDtoRs,
    PageDtoRsServiceProviderDetailDtoRs,
    PageDtoRsServiceProviderSearchDtoRs,
    ServiceProviderDetailDtoRs,
)

app = FastAPI(
    title='Сервис платежей "Поисковые сервисы каталога поставщиков услуг" (Хакатон)',
    description="Поисковые сервисы каталога поставщиков услуг",
    version="1.0.14",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi/rb/pmnt/catalog/hackathon/v1"}],
)


@app.get(
    "/catalog/categories",
    response_model=PageDtoRsCategoryDtoRs,
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
def get_categories(
    x__u_n_c: Optional[constr(min_length=0, max_length=64)] = Header(None, alias="X-UNC"),
    client_unc: Optional[constr(min_length=0, max_length=64)] = Query(None, alias="clientUnc"),
    x__c_l_i_e_n_t__c_h_a_n_n_e_l: Optional[XCLIENTCHANNEL2] = Header(None, alias="X-CLIENT-CHANNEL"),
    x__l_o_g_i_n__m_o_d_e: Optional[constr(min_length=0, max_length=32)] = Header(None, alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: Optional[constr(min_length=0, max_length=128)] = Header(None, alias="X-ROLES"),
    x__p_a_r_t_n_e_r__i_d: Optional[constr(min_length=0, max_length=64)] = Header(None, alias="X-PARTNER-ID"),
    operation_page_size: Optional[conint(ge=0, le=1000)] = Query(0, alias="operationPageSize"),
    region_id: Optional[constr(min_length=0, max_length=3)] = Query(None, alias="regionId"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
) -> Union[PageDtoRsCategoryDtoRs, GenericError]:
    """
    Получение доступных категорий услуг ПУ
    """
    return create_factory_class(PageDtoRsCategoryDtoRs).build()


@app.get(
    "/catalog/operations",
    response_model=PageDtoRsServiceProviderSearchDtoRs,
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
def find_operations(
    x__u_n_c: Optional[constr(min_length=0, max_length=64)] = Header(None, alias="X-UNC"),
    client_unc: Optional[constr(min_length=0, max_length=64)] = Query(None, alias="clientUnc"),
    x__c_l_i_e_n_t__c_h_a_n_n_e_l: Optional[XCLIENTCHANNEL5] = Header(None, alias="X-CLIENT-CHANNEL"),
    x__l_o_g_i_n__m_o_d_e: Optional[constr(min_length=0, max_length=32)] = Header(None, alias="X-LOGIN-MODE"),
    x__r_o_l_e_s: Optional[constr(min_length=0, max_length=255)] = Header(None, alias="X-ROLES"),
    x__p_a_r_t_n_e_r__i_d: Optional[constr(min_length=0, max_length=64)] = Header(None, alias="X-PARTNER-ID"),
    category_id: Optional[constr(min_length=0, max_length=16)] = Query(None, alias="categoryId"),
    region_id: Optional[constr(min_length=0, max_length=3)] = Query(None, alias="regionId"),
    filter: Optional[constr(min_length=0, max_length=255)] = None,
    sub_types: Optional[constr(min_length=0, max_length=255)] = Query(None, alias="subTypes"),
    actions: Optional[constr(min_length=0, max_length=255)] = None,
    page_number: Optional[constr(max_length=6)] = Query(None, alias="pageNumber"),
    page_size: Optional[constr(max_length=4)] = Query(None, alias="pageSize"),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
) -> Union[PageDtoRsServiceProviderSearchDtoRs, GenericError]:
    """
    Поиск услуг ПУ
    """
    return create_factory_class(PageDtoRsServiceProviderSearchDtoRs).build()


@app.get(
    "/catalog/operations/list",
    response_model=PageDtoRsServiceProviderDetailDtoRs,
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
def find_operations_1(
    ids: constr(min_length=0, max_length=2000),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
) -> Union[PageDtoRsServiceProviderDetailDtoRs, GenericError]:
    """
    Получение услуг ПУ по списку ID
    """
    return create_factory_class(PageDtoRsServiceProviderDetailDtoRs).build()


@app.get(
    "/catalog/operations/{id}",
    response_model=ServiceProviderDetailDtoRs,
    responses={
        "400": {"model": GenericError},
        "401": {"model": GenericError},
        "404": {"model": GenericError},
        "422": {"model": GenericError},
        "429": {"model": GenericError},
        "500": {"model": GenericError},
        "503": {"model": GenericError},
        "504": {"model": GenericError},
    },
)
def get_operation(
    id: constr(min_length=0, max_length=32),
    x__global__transaction__i_d: Optional[constr(max_length=24)] = Header(None, alias="X-Global-Transaction-ID"),
    authorization: constr(max_length=5000) = Header(..., alias="Authorization"),
) -> Union[ServiceProviderDetailDtoRs, GenericError]:
    """
    Получение услуги ПУ по ID
    """
    return create_factory_class(ServiceProviderDetailDtoRs).build()
