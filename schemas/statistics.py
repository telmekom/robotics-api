from typing import Dict, List, Optional
from pydantic import BaseModel

from schemas.base import BaseResponse

# Shop

class ShopStatisticsInfo(BaseModel):
    lively_count: Optional[int] = None
    total_count: Optional[int] = None
    new_count: Optional[int] = None
    lively_rate: Optional[int] = None

class ShopStatistics(BaseModel):
    shop_id: Optional[int] = None
    shop_name: Optional[str] = None
    run_count: Optional[int] = None
    bind_count: Optional[int] = None
    duration: Optional[float] = None
    stop_duration: Optional[float] = None

class ShopStatisticsData(BaseModel):
    summary: Optional[ShopStatisticsInfo] = None
    qoq: Optional[ShopStatisticsInfo] = None
    lively_top10: Optional[List[ShopStatistics]] = None
    silent_top10: Optional[List[ShopStatistics]] = None

class ShopStatisticsResponse(BaseResponse):
    data: Optional[ShopStatisticsData] = None

# Robot

class RobotStatisticsInfo(BaseModel):
    boot_count: Optional[int] = None
    total_count: Optional[int] = None
    bind_count: Optional[int] = None
    active_count: Optional[int] = None
    lively_rate: Optional[float] = None

class RobotStatistics(BaseModel):
    product_code: Optional[str] = None
    bind_count: Optional[int] = None
    active_count: Optional[int] = None
    bind_rate: Optional[float] = None
    active_rate: Optional[int] = None
    
class RobotStatisticsData(BaseModel):
    summary: Optional[RobotStatisticsInfo] = None
    qoq: Optional[RobotStatisticsInfo] = None
    chart: Optional[Dict[str, RobotStatistics]]

class RobotStatisticsResponse(BaseResponse):
    data: Optional[RobotStatisticsData] = None


# Robot Ops

class RobotOpsStatistics(BaseModel):
    duration: Optional[float] = None
    mileage: Optional[float] = None
    task_count: Optional[int] = None
    area: Optional[float] = None

class RobotOpsStatisticsData(BaseModel):
    summary: Optional[RobotOpsStatistics] = None
    qoq: Optional[RobotOpsStatistics] = None

class RobotOpsStatisticsResponse(BaseResponse):
    data: Optional[RobotOpsStatisticsData] = None