from typing import Dict, List, Union
from pydantic import BaseModel

# Robot List

class RobotListItem(BaseModel):
    mac: str
    shop_id: str
    shop_name: str
    sn: str
    product_code: str

class RobotListData(BaseModel):
    count: int
    list: list[RobotListItem]

class RobotListResponse(BaseModel):
    data: RobotListData
    message: str
    trace_id: str

# Robot Analysis

class RobotAnalysisChartItem(BaseModel):
    task_time: Union[str, None] = None
    product_code: Union[int, None] = None
    run_count: Union[int, None] = None

class RobotAnalysisChart(BaseModel):
    task_time: Union[str, None] = None
    run_count: Union[int, None] = None
    list: List[RobotAnalysisChartItem]

class RobotAnalysisData(BaseModel):
    chart: List[RobotAnalysisChart]
    qoq_chart: List[RobotAnalysisChart]

class RobotAnalysisResponse(BaseModel):
    message: Union[str, None] = None
    data: Union[RobotAnalysisData, None] = None
    trace_id: Union[str, None] = None

# Robot Statistics

class RobotStatisticsDataItem(BaseModel):
    boot_count: Union[int, None] = None
    total_count: Union[int, None] = None
    bind_count: Union[int, None] = None
    active_count: Union[int, None] = None
    lively_rate: Union[float, None] = None

class RobotStatisticsChartItem(BaseModel):
    product_code: Union[str, None] = None
    bind_count: Union[int, None] = None
    active_count: Union[int, None] = None
    bind_rate: Union[float, None] = None
    active_rate: Union[int, None] = None

class RobotStatisticsChart(BaseModel):
    chart: Dict[str, RobotStatisticsChartItem] = {}

class RobotStatisticsData(BaseModel):
    summary: Union[RobotStatisticsDataItem, None] = None
    qoq: Union[RobotStatisticsDataItem, None] = None
    chart: Union[RobotStatisticsChart, None] = None

class RobotStatisticsResponse(BaseModel):
    message: Union[str, None] = None
    data: Union[RobotStatisticsData, None] = None
    trace_id: Union[str, None] = None


# Robot Ops Statistics

class RobotOpsStatisticsDataItem(BaseModel):
    duration: Union[float, None] = None
    mileage: Union[float, None] = None
    task_count: Union[int, None] = None
    area: Union[int, None] = None

class RobotOpsStatisticsData(BaseModel):
    summary: Union[RobotOpsStatisticsDataItem, None] = None
    qoq: Union[RobotOpsStatisticsDataItem, None] = None

class RobotOpsStatisticsResponse(BaseModel):
    message: Union[str, None] = None
    data: Union[RobotOpsStatisticsData, None] = None
    trace_id: Union[str, None] = None

# Robot Position 

class RobotPositionVector(BaseModel):
    x: Union[float, None] = None
    y: Union[float, None] = None
    z: Union[float, None] = None

class RobotPositionData(BaseModel):
    map_name: Union[str, None] = None
    floor: Union[str, None] = None
    position: Union[RobotPositionVector, None] = None

class RobotPositionResponse(BaseModel):
    message: Union[str, None] = None
    data: Union[RobotPositionData, None] = None
    trace_id: Union[str, None] = None
