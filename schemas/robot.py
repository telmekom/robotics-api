from typing import List, Union
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
    chart: list[str, RobotStatisticsChartItem]

class RobotStatisticsData(BaseModel):
    summary: RobotStatisticsDataItem
    qoq: RobotStatisticsDataItem
    chart: RobotStatisticsChart

class RobotStatisticsResponse(BaseModel):
    message: Union[str, None] = None
    data: Union[RobotStatisticsData, None] = None
    trace_id: Union[str, None] = None
