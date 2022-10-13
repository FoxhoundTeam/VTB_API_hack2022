from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, constr


class Code(str, Enum):
    code_400 = "400"
    code_401 = "401"
    code_403 = "403"
    code_422 = "422"
    code_429 = "429"
    code_500 = "500"
    code_503 = "503"
    code_504 = "504"


class GenericError(BaseModel):
    httpCode: Code = Field(..., description="HTTP code", example="400")
    httpMessage: Optional[constr(max_length=24)] = Field(None, description="HTTP Message", example="Bad Request")
    moreInformation: Optional[constr(max_length=60000)] = Field(
        None, description="Extended Message", example="Bad Request"
    )
