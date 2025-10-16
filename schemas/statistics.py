from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel

from schemas.base import BaseResponse

# Shop

class ShopStatisticsInfo(BaseModel):
    lively_count: Optional[int]
    total_count: Optional[int]
    new_count: Optional[int]
    lively_rate: Optional[int]

class ShopStatistics(BaseModel):
    shop_id: Optional[int]
    shop_name: Optional[int]
    run_count: Optional[int]
    bind_count: Optional[int]
    duration: Optional[float]
    stop_duration: Optional[float]

class ShopStatisticsData(BaseModel):
    summary: Optional[ShopStatisticsInfo]
    qoq: Optional[ShopStatisticsInfo]
    lively_top10: Optional[List[ShopStatistics]]
    silent_top10: Optional[List[ShopStatistics]]

class ShopStatisticsResponse(BaseResponse):
    data: Optional[ShopStatisticsData]

# Robot

class RobotStatisticsInfo(BaseModel):
    boot_count: Optional[int]
    total_count: Optional[int]
    bind_count: Optional[int]
    active_count: Optional[int]
    lively_rate: Optional[float]

class RobotStatistics(BaseModel):
    product_code: Optional[str]
    bind_count: Optional[int]
    active_count: Optional[int]
    bind_rate: Optional[float]
    active_rate: Optional[int]
    
class RobotStatisticsData(BaseModel):
    summary: Optional[RobotStatisticsInfo]
    qoq: Optional[RobotStatisticsInfo]
    chart: Dict[str, RobotStatistics]

class RobotStatisticsResponse(BaseResponse):
    data: Optional[RobotStatisticsData]


# Robot Ops

class RobotOpsStatistics(BaseModel):
    duration: Optional[float]
    mileage: Optional[float]
    task_count: Optional[int]
    area: Optional[int]

class RobotOpsStatisticsData(BaseModel):
    summary: Optional[RobotOpsStatistics]
    qoq: Optional[RobotOpsStatistics]

class RobotOpsStatisticsResponse(BaseResponse):
    data: Optional[RobotOpsStatisticsData]