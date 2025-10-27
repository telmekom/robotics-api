from typing import List, Optional
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
    id: Optional[str] = None
    sn: Optional[str] = None
    mac: Optional[str] = None
    product_code: Optional[str] = None
    upload_time: Optional[str] = None
    task_time: Optional[str] = None
    soft_version: Optional[str] = None
    hard_version: Optional[str] = None
    ip: Optional[str] = None

class RobotCheckResult(BaseModel):
    check_step: Optional[str] = None
    check_state: Optional[str] = None
    check_description: Optional[str] = None

class RobotLog(RobotBaseLog):
    check_result: Optional[List[RobotCheckResult]] = None
    is_success: Optional[int] = None

class RobotLogData(BaseModel):
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    list: List[RobotLog] = []

class RobotLogResponse(BaseResponse):
    data: Optional[RobotLogData] = None

# Log Errors

class RobotErrorLog(RobotBaseLog):
    check_result: Optional[List[RobotCheckResult]] = None
    is_success: Optional[int] = None
    error_level: Optional[str] = None
    error_type: Optional[str] = None
    error_id: Optional[str] = None

class RobotErrorData(BaseModel):
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    list: List[RobotErrorLog] = []

class RobotErrorResponse(BaseResponse):
    data: Optional[RobotErrorData] = None

# Log Charges

class RobotChargeLog(RobotBaseLog):
    charge_power_percent: Optional[int] = None
    charge_duration: Optional[int] = None
    min_power_percent: Optional[int] = None
    max_power_percent: Optional[int] = None

class RobotChargeData(BaseModel):
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    list: List[RobotChargeLog] = []

class RobotChargeResponse(BaseResponse):
    data: Optional[RobotChargeData] = None

# Log Battery

class RobotChangeLog(RobotChargeLog):
    battery_sn: Optional[str] = None
    battery_model: Optional[int] = None
    cycle: Optional[int] = None
    design_capacity: Optional[int] = None
    pack_voltage: Optional[int] = None
    soc: Optional[int] = None
    soh: Optional[int] = None
    full_capacity: Optional[int] = None
    work_status: Optional[int] = None
    current: Optional[int] = None
    cell_temperature: Optional[List[int]] = None
    cell_voltage: Optional[List[int]] = None
    shop_id: Optional[str] = None
    shop_name: Optional[str] = None
    battery_model_name: Optional[str] = None

class RobotChangeData(BaseModel):
    total: Optional[int] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    list: List[RobotChangeLog] = []

class RobotBatteryResponse(BaseResponse):
    data: Optional[RobotChangeData] = None
