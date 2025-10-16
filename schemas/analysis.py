from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field

from schemas.base import BaseResponse

class AnalysisInfos(BaseModel):
    lively_count: Optional[int]
    silent_count: Optional[int]
    new_count: Optional[int]
    total_count: Optional[int]
    task_count: Optional[int]
    area: Optional[float]
    duration: Optional[float]
    power_consumption: Optional[float]
    water_consumption: Optional[float]
    mileage: Optional[float]
    table_count: Optional[int]
    tray_count: Optional[int]
    task_count: Optional[int]
    destination_count: Optional[int]

class AnalysisChartItem(BaseModel):
    task_time: Optional[str]
    lively_count: Optional[int]
    silent_count: Optional[int]
    new_count: Optional[int]
    total_count: Optional[int]
    area: Optional[float]
    duration: Optional[float]
    power_consumption: Optional[float]
    water_consumption: Optional[float]
    task_count: Optional[int]
    mileage: Optional[float]
    table_count: Optional[int]
    tray_count: Optional[int]
    running_task_count: Optional[int]

class AnalysisData(BaseModel):
    summary: Optional[AnalysisInfos]
    qoq: Optional[AnalysisInfos]
    chart: Optional[List[AnalysisChartItem]]
    qoq_chart: Optional[List[AnalysisChartItem]]

class AnalysisResponse(BaseResponse):
    data: Optional[AnalysisData]