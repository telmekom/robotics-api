from tkinter import N
from typing import Any, Dict, List, Union
from pydantic import BaseModel

from schemas.base import BaseResponse

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

class RobotListResponse(BaseResponse):
    data: RobotListData

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

class RobotAnalysisResponse(BaseResponse):
    data: Union[RobotAnalysisData, None] = None

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

class RobotStatisticsResponse(BaseResponse):
    data: Union[RobotStatisticsData, None] = None


# Robot Ops Statistics

class RobotOpsStatisticsDataItem(BaseModel):
    duration: Union[float, None] = None
    mileage: Union[float, None] = None
    task_count: Union[int, None] = None
    area: Union[int, None] = None

class RobotOpsStatisticsData(BaseModel):
    summary: Union[RobotOpsStatisticsDataItem, None] = None
    qoq: Union[RobotOpsStatisticsDataItem, None] = None

class RobotOpsStatisticsResponse(BaseResponse):
    data: Union[RobotOpsStatisticsData, None] = None

# Robot Position 

class RobotPositionVector(BaseModel):
    x: Union[float, None] = None
    y: Union[float, None] = None
    z: Union[float, None] = None

class RobotPositionData(BaseModel):
    map_name: Union[str, None] = None
    floor: Union[str, None] = None
    position: Union[RobotPositionVector, None] = None

class RobotPositionResponse(BaseResponse):
    data: Union[RobotPositionData, None] = None

# Robot Cleaning Task List

class RobotCleaningTaskListBackPoint(BaseModel):
    floor: str
    map_name: str
    point_name: str
    point_id: str

class RobotCleaningTaskListStationConfig(BaseModel):
    id: str
    station_name: str
    station_type: Union[int, None] = None
    station_funtion: int
    map_name: str

class RobotCleaningTaskListConfig(BaseModel):
    isopen: bool
    scale: int

class RobotCleaningTaskListItem(BaseModel):
    task_id: str
    version: int
    name: str
    desc: str
    config: Dict[str, Any]
    floor_list: List[Dict[str, Any]]
    status: int
    is_single_task: Union[bool, None] = None
    task_count: Union[int, None] = None
    task_mode: Union[int, None] = None
    back_point: Union[RobotCleaningTaskListBackPoint, None] = None
    pre_clean_time: Union[int, None] = None
    is_area_connect: Union[bool, None] = None
    station_config: Union[RobotCleaningTaskListStationConfig, None] = None
    cleanagent_config: Union[RobotCleaningTaskListConfig, None] = None
    is_hand_sort: Union[bool, None] = None

class RobotCleaningTaskListData(BaseModel):
    count: int
    item: list[RobotCleaningTaskListItem]

class RobotCleaningTaskListResponse(BaseResponse):
    data: Union[RobotCleaningTaskListData, None] = None

# Robot Cleaning Detail

class RobotCleaningDetailPosition(BaseModel):
    x: float
    y: float
    z: float

class RobotCleaningDetailBreakPoint(BaseModel):
    index: int
    vector: RobotCleaningDetailPosition
    clean_type: Union[int, None] = None
    start: Union[Dict[str, Any], None] = None

class RobotCleaningDetailTaskStatus(BaseModel):
    time: int
    area: int
    status: int
    break_point: Union[RobotCleaningDetailBreakPoint, None] = None
    percentage: Union[int, None] = None
    remaining_time: Union[int, None] = None
    task_area: Union[float, None] = None
    cost_water: Union[int, None] = None
    cost_battery: Union[int, None] = None
    charge_count: Union[int, None] = None

class RobotCleaningDetailCleanMode(BaseModel):
    mode: int
    report_id: str
    msg: str
    result: RobotCleaningDetailTaskStatus
    task: Union[Dict[str, Any], None] = None
    map: Union[Dict[str, Any], None] = None
    config: Dict[str, Any]

class RobotCleaningDetailCleanBot(BaseModel):
    rising: int
    sewage: int
    task: int
    clean: Union[RobotCleaningDetailCleanMode, None] = None

class RobotCleaningDetailShop(BaseModel):
    id: int
    name: str

class RobotCleaningDetailData(BaseModel):
    mac: str
    nickname: str
    online: bool
    battery: int
    map: Dict[str, Any]
    cleanbot: RobotCleaningDetailCleanBot
    shop: RobotCleaningDetailShop
    position: RobotCleaningDetailPosition

class RobotCleaningDetailResponse(BaseResponse):
    data: Union[RobotCleaningDetailData, None] = None
