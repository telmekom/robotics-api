from fastapi import Query, APIRouter
import requests
from schemas.robot import RobotCleaningDetailResponse, RobotCleaningScheduledTaskResponse, RobotCleaningTaskListResponse, RobotListResponse, RobotPositionResponse
from shared.pudu_api_helper import build_headers_with_hmac, clean_and_encode_params, generate_get_header_block
import os
from dotenv import load_dotenv
from examples.robots import robots_example, robots_cleaning_tasks_example, robot_cleaning_detail_example
load_dotenv()  

router = APIRouter(
    tags=["Robots"],
)

@router.get("/robots", response_model=RobotListResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robots_example
            }
        }
    },
})
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

@router.get("/robots/get-position", response_model=RobotPositionResponse)
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

@router.get("/robots/cleaning/tasks", response_model=RobotCleaningTaskListResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robots_cleaning_tasks_example
            }
        }
    },
})
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
        
@router.get("/robots/cleaning/detail", response_model=RobotCleaningDetailResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robot_cleaning_detail_example
            }
        }
    },
})
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

@router.get("/robots/cleaning/scheduled-tasks", response_model=RobotCleaningScheduledTaskResponse)
def get_robot_cleaning_scheduled_task_list(
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


