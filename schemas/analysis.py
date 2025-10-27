from typing import List, Optional
from pydantic import BaseModel

from schemas.base import BaseResponse

class AnalysisInfos(BaseModel):
    lively_count: Optional[int] = None
    silent_count: Optional[int] = None
    new_count: Optional[int] = None
    total_count: Optional[int] = None
    task_count: Optional[int] = None
    area: Optional[float] = None
    duration: Optional[float] = None
    power_consumption: Optional[float] = None
    water_consumption: Optional[float] = None
    mileage: Optional[float] = None
    table_count: Optional[int] = None
    tray_count: Optional[int] = None
    task_count: Optional[int] = None
    destination_count: Optional[int] = None

class AnalysisChartItem(BaseModel):
    task_time: Optional[str] = None
    lively_count: Optional[int] = None
    silent_count: Optional[int] = None
    new_count: Optional[int] = None
    total_count: Optional[int] = None
    area: Optional[float] = None
    duration: Optional[float] = None
    power_consumption: Optional[float] = None
    water_consumption: Optional[float] = None
    task_count: Optional[int] = None
    mileage: Optional[float] = None
    table_count: Optional[int] = None
    tray_count: Optional[int] = None
    running_task_count: Optional[int] = None

class AnalysisData(BaseModel):
    summary: Optional[AnalysisInfos] = None
    qoq: Optional[AnalysisInfos] = None
    chart: Optional[List[AnalysisChartItem]] = None
    qoq_chart: Optional[List[AnalysisChartItem]] = None

class AnalysisResponse(BaseResponse):
    data: Optional[AnalysisData] = None

class CleaningAnalysisResponse(BaseResponse):
    chart: Optional[List[AnalysisChartItem]]