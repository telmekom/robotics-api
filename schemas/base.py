from typing import List, Union
from pydantic import BaseModel

class BaseResponse(BaseModel):
    data: None
    message: str
    trace_id: str
    code: Union[int, None]