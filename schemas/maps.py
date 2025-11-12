from typing import List, Optional
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


class MapDetailsZoneNode(BaseModel):
    vector_list: List[float]

class MapDetailsZone(BaseModel):
    id: str
    name: str
    zone_node_list: List[MapDetailsZoneNode]

class MapDetailsCleanPath(BaseModel):
    x: float
    y: float
    z: float

class MapDetailsElement(BaseModel):
    id: str
    name: str
    type: str
    vector_list: List[float]
    mode: str
    clean_path_list: List[MapDetailsCleanPath]
    zone_list:  Optional[List[MapDetailsZone]] = []

class MapDetailsData(BaseModel):
    map_name: str
    url: str
    width: int
    height: int
    resolution: float
    origin_list: List[float]
    scale_ratio: float
    canvas_translate_x: float
    canvas_translate_y: float
    element_list: Optional[List[MapDetailsElement]] = []


class MapDetailsResponse(BaseResponse):
    data: MapDetailsData