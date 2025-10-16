from tkinter import N
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel

from schemas.base import BaseResponse, Vector3

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

# Robot Position 

class RobotPositionData(BaseModel):
    map_name: Union[str, None] = None
    floor: Union[str, None] = None
    position: Union[Vector3, None] = None

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

class RobotCleaningDetailBreakPoint(BaseModel):
    index: int
    vector: Vector3
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
    position: Vector3

class RobotCleaningDetailResponse(BaseResponse):
    data: Union[RobotCleaningDetailData, None] = None

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
    back_point: Optional[Dict[str, Any]]
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