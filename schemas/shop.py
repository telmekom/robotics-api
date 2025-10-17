from typing import List, Optional, Union
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


# Logs

class RobotBaseLog(BaseModel):
    id: Optional[str]
    sn: Optional[str]
    mac: Optional[str]
    product_code: Optional[str]
    upload_time: Optional[str]
    task_time: Optional[str]
    soft_version: Optional[str]
    hard_version: Optional[str]
    ip: Optional[str]

class RobotCheckResult(BaseModel):
    check_step: Optional[str]
    check_state: Optional[str]
    check_description: Optional[str]

class RobotLog(RobotBaseLog):
    check_result: Optional[List[RobotCheckResult]]
    is_success: Optional[int]

class RobotLogData(BaseModel):
    total: Optional[int]
    limit: Optional[int]
    offset: Optional[int]
    list: List[RobotLog]

class RobotLogResponse(BaseResponse):
    data: Optional[RobotLogData]

# Log Errors

class RobotErrorLog(RobotBaseLog):
    check_result: Optional[List[RobotCheckResult]]
    is_success: Optional[int]
    error_level: Optional[str]
    error_type: Optional[str]
    error_id: Optional[str]

class RobotErrorData(BaseModel):
    total: Optional[int]
    limit: Optional[int]
    offset: Optional[int]
    list: List[RobotErrorLog]

class RobotErrorResponse(BaseResponse):
    data: Optional[RobotErrorData]

# Log Charges

class RobotChargeLog(RobotBaseLog):
    charge_power_percent: Optional[int]
    charge_duration: Optional[int]
    min_power_percent: Optional[int]
    max_power_percent: Optional[int]

class RobotChargeData(BaseModel):
    total: Optional[int]
    limit: Optional[int]
    offset: Optional[int]
    list: List[RobotChargeLog]

class RobotChargeResponse(BaseResponse):
    data: Optional[RobotChargeData]

# Log Battery

class RobotChangeLog(RobotChargeLog):
    battery_sn: Optional[str]
    battery_model: Optional[int]
    cycle: Optional[int]
    design_capacity: Optional[int]
    pack_voltage: Optional[int]
    soc: Optional[int]
    soh: Optional[int]
    full_capacity: Optional[int]
    work_status: Optional[int]
    current: Optional[int]
    cell_temperature: Optional[List[int]]
    cell_voltage: Optional[List[int]]
    shop_id: Optional[str]
    shop_name: Optional[str]
    battery_model_name: Optional[str]

class RobotChangeData(BaseModel):
    total: Optional[int]
    limit: Optional[int]
    offset: Optional[int]
    list: List[RobotChangeLog]

class RobotBatteryResponse(BaseResponse):
    data: Optional[RobotChangeData]
