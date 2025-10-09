from typing import List, Union
from pydantic import BaseModel, field_validator

# Robot List

class RobotListItem(BaseModel):
    mac: str
    shop_id: str
    shop_name: str
    sn: str
    product_code: str

    # @field_validator('shop_name')
    # def validate_shop_name(cls, value):
    #     # EXAMPLE OF VALIDATION
    #     if len(value) > 50:
    #         raise ValueError("Shop name must be less than 50 characters")
    #     return value

class RobotListData(BaseModel):
    count: int
    list: list[RobotListItem]

class RobotListResponse(BaseModel):
    data: RobotListData
    message: str
    trace_id: str

# Robot Analysis

class RobotAnalysisChartItem(BaseModel):
    task_time: str
    product_code: int
    run_count: int

class RobotAnalysisChart(BaseModel):
    task_time: str
    run_count: int
    list: List[RobotAnalysisChartItem]

class RobotAnalysisData(BaseModel):
    chart: List[RobotAnalysisChart]
    qoq_chart: List[RobotAnalysisChart]

class RobotAnalysisResponse(BaseModel):
    message: Union[str, None] = None
    data: Union[RobotAnalysisData, None] = None
    trace_id: Union[str, None] = None
