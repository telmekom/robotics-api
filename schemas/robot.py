from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel

from schemas.base import BaseResponse, Vector3


class RobotPositionData(BaseModel):
    map_name: Optional[str] = None
    point_name: Optional[str] = None
    floor: Optional[str] = None
    position: Optional[Vector3] = None
    point_id: Optional[str] = None

class RobotInfos(BaseModel):
    mac: str
    shop_id: str
    shop_name: str
    sn: str
    product_code: str


# Robot List

class RobotListData(BaseModel):
    count: int
    list: List[RobotInfos]

class RobotListResponse(BaseResponse):
    data: Optional[RobotListData] = None

# Robot Position 

class RobotPositionResponse(BaseResponse):
    data: Optional[RobotPositionData] = None

# Robot Cleaning Task List

class RobotCleaningTaskListStationConfig(BaseModel):
    id: str
    station_name: str
    station_type: Optional[int] = None
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
    is_single_task: Optional[bool] = None
    task_count: Optional[int] = None
    task_mode: Optional[int] = None
    back_point: Optional[RobotPositionData] = None
    pre_clean_time: Optional[int] = None
    is_area_connect: Optional[bool] = None
    station_config: Optional[RobotCleaningTaskListStationConfig] = None
    cleanagent_config: Optional[RobotCleaningTaskListConfig] = None
    is_hand_sort: Optional[bool] = None

class RobotCleaningTaskListData(BaseModel):
    count: int
    item: list[RobotCleaningTaskListItem]

class RobotCleaningTaskListResponse(BaseResponse):
    data: Optional[RobotCleaningTaskListData] = None

# Robot Cleaning Detail

class RobotCleaningDetailBreakPoint(BaseModel):
    index: int
    vector: Vector3
    clean_type: Optional[int] = None
    start: Optional[Dict[str, Any]] = None

class RobotCleaningDetailTaskStatus(BaseModel):
    time: int
    area: float
    status: int
    break_point: Optional[RobotCleaningDetailBreakPoint] = None
    percentage: Optional[int] = None
    remaining_time: Optional[int] = None
    task_area: Optional[float] = None
    cost_water: Optional[int] = None
    cost_battery: Optional[int] = None
    charge_count: Optional[int] = None

class RobotCleaningDetailCleanMode(BaseModel):
    mode: int
    report_id: str
    msg: str
    result: RobotCleaningDetailTaskStatus
    task: Optional[Dict[str, Any]] = None
    map: Optional[Dict[str, Any]] = None
    config: Dict[str, Any]

class RobotCleaningDetailCleanBot(BaseModel):
    rising: int
    sewage: int
    task: int
    clean: Optional[RobotCleaningDetailCleanMode] = None

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
    position: Vector3

class RobotCleaningDetailResponse(BaseResponse):
    data: Optional[RobotCleaningDetailData] = None

# Robot Cleaning Scheduled Task List

class RobotCleaningScheduledTaskListMap(BaseModel):
    name: str
    lv: int
    floor: str

class RobotCleaningScheduledTask(BaseModel):
    task_id: str
    task_version: int
    name: str
    task_desc: str
    pre_clean_time: int
    clean_area: float
    map: List[RobotCleaningScheduledTaskListMap]
    clean_mode: int
    back_point: Optional[Dict[str, Any]] = None
    clean_type: int
    mode: int
    product: str

class RobotCleaningScheduledTaskCron(BaseModel):
    cron_id: str
    device_name: str
    pid: str
    hour: int
    minute: int
    weeks: List[int]
    task_list: List[RobotCleaningScheduledTask]
    create_time: int
    update_time: int
    cron_status: str
    keep_time: int
    repeat_clean_time: int

class RobotCleaningScheduledTaskData(BaseModel):
    count: int
    list: List[RobotCleaningScheduledTaskCron]

class RobotCleaningScheduledTaskResponse(BaseResponse):
    data: Union[RobotCleaningScheduledTaskData, None] = None