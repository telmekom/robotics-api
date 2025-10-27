from typing import List
from pydantic import BaseModel

from schemas.base import BaseResponse

# Map List

class Map(BaseModel):
    map_name: str

class MapListData(BaseModel):
    count: int
    list: List[Map] = []

class MapListResponse(BaseResponse):
    data: MapListData
