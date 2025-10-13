from typing import List, Union
from pydantic import BaseModel

# Map List

class Map(BaseModel):
    map_name: str

class MapListData(BaseModel):
    count: int
    list: List[Map] = []

class MapListResponse(BaseModel):
    data: MapListData
    message: str
    trace_id: str


# Map Detail

class MapDetailResponse(BaseModel):
    message: Union[str, None] = None
    # data: Union[Map, None] = None
    trace_id: Union[str, None] = None