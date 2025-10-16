from typing import Any, List, Union
from pydantic import BaseModel

class BaseResponse(BaseModel):
    data: Any
    message: Union[str, None] = None
    trace_id: Union[str, None] = None
    code: Union[int, None] = None

class Vector3(BaseModel):
    x: float
    y: float
    z: float