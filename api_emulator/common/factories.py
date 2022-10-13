from typing import Type, TypeVar, cast

from pydantic import BaseModel
from pydantic_factories import ModelFactory

ModelFactoryType = TypeVar("ModelFactoryType", bound=ModelFactory)


def create_factory_class(model: Type[BaseModel]) -> Type[ModelFactoryType]:
    return cast(Type[ModelFactoryType], type(model.__name__ + "Factory", (ModelFactory,), {"__model__": model}))
