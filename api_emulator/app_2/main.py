from typing import Union

from fastapi import FastAPI

from common.factories import create_factory_class

from .models import Carloan, CarloanResponse

app = FastAPI(
    title="Заявка на автокредит от физических лиц (Хакатон)",
    description="Заявка позволяет получить решение прескоринга и рассчитать примерный ежемесячный платеж,"
    " исходя из полученных данных о клиенте, сумме и сроке кредита и других данных.",
    version="0.4.4",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi"}],
)


@app.post(
    "/carloan",
    response_model=CarloanResponse,
)
def carloan_carloan_post(body: Carloan) -> Union[CarloanResponse]:
    return create_factory_class(CarloanResponse).build()
