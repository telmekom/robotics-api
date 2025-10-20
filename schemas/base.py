from typing import Any, List, Optional, Union
from pydantic import BaseModel

class BaseResponse(BaseModel):
    message: Optional[Any] = None
    trace_id: Optional[str] = None
    code: Optional[int] = None

class Vector3(BaseModel):
    x: float
    y: float
    z: float