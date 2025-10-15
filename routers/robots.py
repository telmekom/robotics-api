import re
from fastapi import Query, APIRouter
import requests
from schemas.robot import *
from schemas.shop import *
from shared.pudu_api_helper import build_headers_with_hmac, clean_and_encode_params, generate_get_header_block
from shared.time import TimeUnit
import os
from dotenv import load_dotenv
load_dotenv()  

router = APIRouter(
    tags=["Robots"],
    responses={404: {"description": "Robots API for Data, Analytics and Statistics"}}
)

@router.get("/robots", response_model=RobotListResponse)
def get_robots(
        limit: int = Query(10, ge=1), 
        offset: int = Query(0, ge=0),
        shop_id: int | None = Query(None, description="Parent Shop ID, all robots if not specified"),
    ):
        try:
            encoded_params = clean_and_encode_params({
                    "limit": limit, 
                    "offset": offset, 
                    "shop_id": shop_id, 
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-open-platform-service/v1/api/robot?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/robots/analysis", response_model=RobotAnalysisResponse)
def get_robot_analysis(start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = None, 
        time_unit: TimeUnit = Query(TimeUnit.DAY, description="Granularity of the charts", examples=[TimeUnit.DAY, TimeUnit.HOUR]),
        timezone_offset: int = 0
    ):
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset,
                "time_unit": time_unit.value
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/run?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/robots/statistics", response_model=RobotStatisticsResponse)
def get_robot_statistics(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(description="Robot Shop ID"),
        timezone_offset: int = Query(0, description="GMT offset (GMT-12 to GMT+14)", ge=-12, le=14),
    ):
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/brief/robot?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/robot-ops/statistics", response_model=RobotOpsStatisticsResponse)
def get_robot_ops_statistics(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(description="Robot Shop ID"),
        timezone_offset: int = Query(0, description="GMT offset (GMT-12 to GMT+14)", ge=-12, le=14),
    ):

        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset,
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/brief/run?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
        
@router.get("/robots/get_position", response_model=RobotPositionResponse)
def get_robot_position(
        sn: str = Query(description="Robot Serial Number"),
    ):
        try:
            encoded_params = clean_and_encode_params({
                "sn": sn, 
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/open-platform-service/v1/robot/get_position?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/robots/cleaning/tasks", response_model=RobotCleaningTaskListResponse)
def get_robot_cleaning_tasks(
        shop_id: int | None = Query(None, description="Shop/Store ID - this or sn must be specified"),
        sn: str | None = Query(None, description="Robot Serial Number - this or shop_id must be specified"),
        # product: list[str] | None = Query(description="Product Type - can be used for CleanBot, MT1, MT1Pro, MT1Max"),
        # mode: list[int] | None = Query(description="1: manual, 2: automatic, 3: inspection+mixed"),
    ):
        try:
            encoded_params = clean_and_encode_params({
                 "shop_id": shop_id,
                "sn": sn, 
            })
            
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/cleanbot-service/v1/api/open/task/list?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
        
@router.get("/robots/cleaning/detail", response_model=RobotCleaningDetailResponse)
def get_robot_cleaning_detail(
        sn: str = Query(description="Robot Serial Number"),
    ):
        try:
            encoded_params = clean_and_encode_params({
                "sn": sn, 
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/cleanbot-service/v1/api/open/robot/detail?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

# [ToDo] SEND COMMAND PUT

@router.get("/robots/cleaning/scheduled-tasks", response_model=RobotCleaningScheduledTaskResponse)
def get_robot_cleaning_detail(
        sn: str = Query(description="Robot Serial Number"),
        limit: int = Query(10, ge=1), 
        offset: int = Query(0, ge=0),
    ):
        try:
            encoded_params = clean_and_encode_params({
                "sn": sn, 
                "limit": limit, 
                "offset": offset
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/cleanbot-service/v1/api/open/cron/list?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}