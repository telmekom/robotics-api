from typing import List, Union
from pydantic import BaseModel

from schemas.base import BaseResponse

# Shop List

class Shop(BaseModel):
    company_id: int
    company_name: str
    shop_id: int
    shop_name: str

class ShopListData(BaseModel):
    count: int
    list: List[Shop]

class ShopListResponse(BaseResponse):
    data: ShopListData

# Shop Analysis

class ChartItem(BaseModel):
    task_time: Union[str, None] = None
    lively_count: Union[int, None] = None
    silent_count: Union[int, None] = None
    new_count: Union[int, None] = None
    total_count: Union[int, None] = None

class AnalysisItem(BaseModel):
    lively_count: Union[int, None] = None
    silent_count: Union[int, None] = None
    new_count: Union[int, None] = None
    total_count: Union[int, None] = None

class ShopAnalysisData(BaseModel):
    summary: Union[AnalysisItem, None] = None
    qoq: Union[AnalysisItem, None] = None
    chart: List[ChartItem]
    qoq_chart: List[ChartItem]

class ShopAnalysisResponse(BaseResponse):
    data: Union[ShopAnalysisData, None] = None

# Shop Statictics

class CountItem(BaseModel):
    lively_count: Union[int, None] = None
    total_count: Union[int, None] = None
    new_count: Union[int, None] = None
    lively_rate: Union[int, None] = None

class ShopStatistics(BaseModel):
    shop_id: Union[int, None] = None
    shop_name: Union[str, None] = None
    run_count: Union[int, None] = None
    bind_count: Union[int, None] = None
    duration: Union[float, None] = None
    stop_duration: Union[float, None] = None

class ShopStatisticsData(BaseModel):
    lively_count: Union[CountItem, None] = None
    qoq: Union[CountItem, None] = None
    lively_top10: list[ShopStatistics]
    silent_top10: list[ShopStatistics]

class ShopStatisticsResponse(BaseResponse):
    data: Union[ShopStatisticsData, None] = None