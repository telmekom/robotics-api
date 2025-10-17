from typing import Any, List, Optional, Union
from pydantic import BaseModel

class BaseResponse(BaseModel):
    message: Optional[Any]
    trace_id: Optional[str]
    code: Optional[int]

class Vector3(BaseModel):
    x: float
    y: float
    z: float