from fastapi import Depends, Query, APIRouter
import requests
from schemas.robot import RobotCleaningDetailResponse, RobotCleaningScheduledTaskResponse, RobotCleaningTaskListResponse, RobotDeliveryTaskResponse, RobotListResponse, RobotPositionResponse
from shared.pudu_api_helper import HACKATHON_API_KEY, EntityType, build_headers_with_hmac, call_api, clean_and_encode_params, generate_get_header_block, header_scheme, is_allowed_id, post_call_api
import os
from dotenv import load_dotenv
from examples.robots import robots_example, robots_cleaning_tasks_example, robot_cleaning_detail_example, robot_delivery_tasks_example, robot_delivery_greeter_tasks_example, robot_delivery_recovery_tasks_example, robot_delivery_call_tasks_example,robot_industrial_lifting_tasks_example
load_dotenv()  

router = APIRouter(
    tags=["Robots"],
)

@router.get("/robots", response_model=RobotListResponse, name="Robot List, filtered by Store", description="",  responses={
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
        shop_id: int = Query(description="Parent Shop ID"),
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}

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

@router.get("/robots/get-position", name="Robot Position on Map", description="", response_model=RobotPositionResponse)
def get_robot_position(
        sn: str = Query(description="Robot Serial Number"),
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if not is_allowed_id(EntityType.ROBOT, sn):
             return {"code": 403, "message": "Forbidden: Robot SN not whitelisted"}

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

@router.get("/robots/cleaning/tasks", name="Cleaning Task-List", description="", response_model=RobotCleaningTaskListResponse, responses={
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
        key: str = Depends(header_scheme)
        # product: list[str] | None = Query(description="Product Type - can be used for CleanBot, MT1, MT1Pro, MT1Max"),
        # mode: list[int] | None = Query(description="1: manual, 2: automatic, 3: inspection+mixed"),
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if shop_id and not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        if sn and not is_allowed_id(EntityType.ROBOT, sn):
             return {"code": 403, "message": "Forbidden: Robot SN not whitelisted"}
        
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
        
@router.get("/robots/cleaning/detail", name="Detailed List of Cleaning Tasks per Robot", description="",  response_model=RobotCleaningDetailResponse, responses={
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
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if not is_allowed_id(EntityType.ROBOT, sn):
             return {"code": 403, "message": "Forbidden: Robot SN not whitelisted"}
        
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

@router.get("/robots/cleaning/scheduled-tasks", name="Scheduled Cleaning Task-List", description="", response_model=RobotCleaningScheduledTaskResponse)
def get_robot_cleaning_scheduled_task_list(
        sn: str = Query(description="Robot Serial Number"),
        limit: int = Query(10, ge=1), 
        offset: int = Query(0, ge=0),
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if not is_allowed_id(EntityType.ROBOT, sn):
             return {"code": 403, "message": "Forbidden: Robot SN not whitelisted"}
        
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


@router.get("/robots/delivery/tasks", name="Delivery Task-List", description="", response_model=RobotDeliveryTaskResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robot_delivery_tasks_example
            }
        }
    },
})
def get_robot_delivery_tasks(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(ge=0),
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if shop_id and not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time,
                "end_time": end_time,
                "shop_id": shop_id,
                "offset": offset,
                "limit": limit,
                "timezone_offset": timezone_offset
            })
            
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/task/delivery?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
       
@router.get("/robots/delivery/greeter/tasks", name="Greeter Delivery Task-List", description="", response_model=RobotDeliveryTaskResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robot_delivery_greeter_tasks_example
            }
        }
    },
})
def get_robot_delivery_greeter_tasks(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(ge=0),
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if shop_id and not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time,
                "end_time": end_time,
                "shop_id": shop_id,
                "offset": offset,
                "limit": limit,
                "timezone_offset": timezone_offset
            })
            
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/task/greeter?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
        
@router.get("/robots/delivery/recovery/tasks", name="Return/Recovery Delivery Task-List", description="", response_model=RobotDeliveryTaskResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robot_delivery_recovery_tasks_example
            }
        }
    },
})
def get_robot_delivery_recovery_tasks(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(ge=0),
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if shop_id and not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time,
                "end_time": end_time,
                "shop_id": shop_id,
                "offset": offset,
                "limit": limit,
                "timezone_offset": timezone_offset
            })
            
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/task/recovery?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/robots/delivery/call/tasks", name="Call Delivery Task-List", description="", response_model=RobotDeliveryTaskResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robot_delivery_call_tasks_example
            }
        }
    },
})
def get_robot_delivery_call_tasks(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(ge=0),
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if shop_id and not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time,
                "end_time": end_time,
                "shop_id": shop_id,
                "offset": offset,
                "limit": limit,
                "timezone_offset": timezone_offset
            })
            
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/task/call?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/robots/industrial/lifting/tasks", name="Lifting Task-List", description="", response_model=RobotDeliveryTaskResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": robot_industrial_lifting_tasks_example
            }
        }
    },
})
def get_robot_industrial_lifting_tasks(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int = Query(ge=0),
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if shop_id and not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time,
                "end_time": end_time,
                "shop_id": shop_id,
                "offset": offset,
                "limit": limit,
                "timezone_offset": timezone_offset
            })
            
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/task/lifting?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}


@router.post("/robots/delivery/send_task", name="Send Delivery Task", description="")
def send_robot_delivery_task(
        # sn: str = Query(description="Robot Serial Number"),
        # type: str = Query("NEW", description="NEW|MODIFY"),
        # delivery_sort: str = Query("AUTO", description="AUTO|FIXED"),
        # execute_task: bool = Query(False, description="If robot instantly executes task or waits for confirmation"),
        # #missing "trays" param
    ):
        # if not is_allowed_id(EntityType.ROBOT, sn):
        #     return {"code": 403, "message": "Forbidden: Robot SN not whitelisted"}
        try:
            delivery_sort = "AUTO"
            execute_task = False
            sn = "8SV043224050010"
            type = "NEW"
            trays = [
                {
                    "destinations": [
                        {
                            "points": "2",
                            "id": "2"
                        }
                    ] 
                }
            ]

            {"delivery_sort": delivery_sort, "execute_task": execute_task, "sn": sn, "trays": trays, "type": type }

            url = f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/open-platform-service/v1/position_command'
            response = post_call_api(url, {"delivery_sort": delivery_sort, "execute_task": execute_task, "sn": sn, "trays": trays, "type": type }, os.getenv("API_APP_KEY"), os.getenv("API_APP_SECRET"))

            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}