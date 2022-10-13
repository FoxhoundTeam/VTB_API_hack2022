from fastapi import FastAPI

from common.factories import create_factory_class

from .models import CalculateResponse, CalculatorRequest

app = FastAPI(
    title="Калькулятор автокредита (Хакатон)",
    description="Сервис предоставляет данные для расчета процентной ставки и размера ежемесячного платежа по автокредиту, если в калькуляторе указаны стоимость автомобиля и желаемый срок погашения кредита.",
    version="3.0.1",
    # servers=[{"url": "https://epa.api.vtb.ru/openapi"}],
)


@app.post("/calculate", response_model=CalculateResponse)
def post_calculate(body: CalculatorRequest = None) -> CalculateResponse:
    """
    Calculate
    """
    return create_factory_class(CalculateResponse).build()
