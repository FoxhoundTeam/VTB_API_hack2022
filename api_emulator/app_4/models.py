# generated by fastapi-codegen:
#   filename:  new_yamls/app_7.yaml
#   timestamp: 2022-10-11T21:09:45+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class CarBody(BaseModel):
    alias: Optional[str] = Field("coupe", title="Alias")
    doors: Optional[int] = Field(None, title="Doors")
    photo: Optional[str] = Field(
        "https://tradeins.space/uploads/photo/7035393/3e801bb45f50f466b91ae07c3bda86f55a561735.jpeg",
        title="Photo",
    )
    title: Optional[str] = Field("Купе", title="Title")
    type: Optional[str] = Field("coupe", title="Type")
    typeTitle: Optional[str] = Field("Купе", title="Typetitle")


class CarModelModel(BaseModel):
    absentee: Optional[bool] = Field(False, title="Absentee")
    alias: Optional[str] = Field("2_series", title="Alias")
    id: Optional[int] = Field(None, title="Id")
    prefix: Optional[str] = Field("", title="Prefix")
    title: Optional[str] = Field("2 серии", title="Title")
    titleRus: Optional[str] = Field("2 серии", title="Titlerus")


class CarRenderPhoto(BaseModel):
    height: Optional[int] = Field(None, title="Height")
    path: Optional[str] = Field("https://tradeins.space/uploads/photo/3266975/33_0003_Слой 5.jpg", title="Path")
    width: Optional[int] = Field(None, title="Width")


class Country(BaseModel):
    code: Optional[str] = Field("DE", title="Code")
    id: Optional[int] = Field(None, title="Id")
    title: Optional[str] = Field("Германия", title="Title")


class TransportType(BaseModel):
    alias: Optional[str] = Field("cars", title="Alias")
    id: Optional[int] = Field(None, title="Id")
    title: Optional[str] = Field("Легковые", title="Title")


class CarBrandOnly(BaseModel):
    absentee: Optional[bool] = Field(True, title="Absentee")
    alias: Optional[str] = Field("bmw", title="Alias")
    country: Country
    id: Optional[int] = Field(None, title="Id")
    isOutbound: Optional[bool] = Field(False, title="Isoutbound")
    logo: Optional[str] = Field(
        "http://tradeins.space/uploads/brand/4/35dad01f02c529a28f45cb8d47d089fa1e911639.png",
        title="Logo",
    )
    title: Optional[str] = Field("BMW", title="Title")
    titleRus: Optional[str] = Field("БМВ", title="Titlerus")


class CarModel(BaseModel):
    absentee: Optional[bool] = Field(False, title="Absentee")
    alias: Optional[str] = Field("2_series", title="Alias")
    bodies: List[CarBody] = Field(..., title="Bodies")
    brand: CarBrandOnly
    carId: Optional[str] = Field("n1648837", title="Carid")
    colorsCount: Optional[int] = Field(None, title="Colorscount")
    count: Optional[int] = Field(None, title="Count")
    hasSpecialPrice: Optional[bool] = Field(False, title="Hasspecialprice")
    id: Optional[int] = Field(None, title="Id")
    metallicPay: Optional[int] = Field(None, title="Metallicpay")
    minprice: Optional[int] = Field(None, title="Minprice")
    model: CarModelModel
    ownTitle: Optional[str] = Field("F44", title="Owntitle")
    pearlPay: Optional[int] = Field(None, title="Pearlpay")
    photo: Optional[str] = Field(
        "https://207231.selcdn.ru/locator-media/models_desktop_q90/tradeins.space-uploads-photo-7035393-3e801bb45f50f466b91ae07c3bda86f55a561735.jpeg",
        title="Photo",
    )
    prefix: Optional[str] = Field("", title="Prefix")
    premiumPriceSpecials: Optional[List[str]] = Field(None, title="Premiumpricespecials")
    renderPhotos: Optional[Dict[str, Dict[str, CarRenderPhoto]]] = Field(None, title="Renderphotos")
    sizesPhotos: Optional[Dict[str, str]] = Field(None, title="Sizesphotos")
    specmetallicPay: Optional[int] = Field(None, title="Specmetallicpay")
    title: Optional[str] = Field("2 серии", title="Title")
    titleRus: Optional[str] = Field("2 серии", title="Titlerus")
    transportType: TransportType


class CarBrand(BaseModel):
    absentee: Optional[bool] = Field(True, title="Absentee")
    alias: Optional[str] = Field("bmw", title="Alias")
    country: Country
    currentCarCount: Optional[int] = Field(None, title="Currentcarcount")
    currentModelsTotal: Optional[int] = Field(None, title="Currentmodelstotal")
    generations: Optional[List[str]] = Field(None, title="Generations")
    id: Optional[int] = Field(None, title="Id")
    isOutbound: Optional[bool] = Field(False, title="Isoutbound")
    logo: Optional[str] = Field(
        "http://tradeins.space/uploads/brand/4/35dad01f02c529a28f45cb8d47d089fa1e911639.png",
        title="Logo",
    )
    models: List[CarModel] = Field(..., title="Models")
    title: Optional[str] = Field("BMW", title="Title")
    titleRus: Optional[str] = Field("БМВ", title="Titlerus")


class Marketplace(BaseModel):
    list: List[CarBrand] = Field(..., title="List")