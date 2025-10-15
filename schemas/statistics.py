from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel

from schemas.base import BaseResponse

class StatisticsChartItem(BaseModel):  
    product_code: Optional[str]
    bind_count: Optional[int]
    active_count: Optional[int]
    bind_rate: Optional[float]
    active_rate: Optional[float]

class StatisticsInfos(BaseModel):
    lively_count: Optional[int]
    boot_count: Optional[int]
    new_count: Optional[int]
    total_count: Optional[int]
    bind_count: Optional[int]
    active_count: Optional[int]
    lively_rate: Optional[float]

class StatisticsData(BaseModel):
    summary: Optional[StatisticsInfos]
    qoq: Optional[StatisticsInfos]
    chart: Optional[Dict[str, StatisticsChartItem]]


class StatisticsResponse(BaseResponse):
    data: Optional[StatisticsData]
