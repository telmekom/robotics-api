from fastapi import Depends, Query, APIRouter
import requests
from schemas.shop import RobotChargeResponse, RobotErrorResponse, RobotLogResponse, ShopListResponse
from shared.pudu_api_helper import HACKATHON_API_KEY, build_headers_with_hmac, clean_and_encode_params, generate_get_header_block, header_scheme
import os
from dotenv import load_dotenv
from examples.shops import shops_example, shops_robotstatus_example, shops_roboterrors_example, shops_robotcharges_example
load_dotenv()  

router = APIRouter(
    tags=["Shops"],
)

@router.get("/shops", response_model=ShopListResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": shops_example
            }
        }
    },
})
def get_shops(
        limit: int = Query(10, ge=1), 
        offset: int = Query(0, ge=0),
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}

        encoded_params = clean_and_encode_params({
            "limit": limit, 
            "offset": offset, 
        })
        
        try:
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-open-platform-service/v1/api/shop?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/shops/robot-status", response_model=RobotLogResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": shops_robotstatus_example
            }
        }
    },
})
def get_shops_robot_status(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        check_step: str | None = Query(None, description="f.ex. CheckCAN, CheckESP, CheckRGBD, CheckLidar, CheckMap, Finish"), 
        is_success: int | None = Query(None, description=" 0: failed (with exception), 1: succeeded, -1 did not filter", examples=[0, 1, -1]),
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        
        encoded_params = clean_and_encode_params({
            "start_time": start_time, 
            "end_time": end_time, 
            "shop_id": shop_id, 
            "offset": offset, 
            "limit": limit, 
            "check_step": check_step, 
            "is_success": is_success, 
            "timezone_offset": timezone_offset
        })
        
        try:
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/log/boot/query_list?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/shops/robot-errors", response_model=RobotErrorResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": shops_roboterrors_example
            }
        }
    },
})
def get_shops_robot_errors(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        error_levels: str | None = Query(None, description="Fault level screening, multiple separated by commas. (Fatal|Error|Warning|Event"), 
        error_types: str | None = Query(None, description="Fault type filtering, multiple separated by commas (LostBattery|LostCamera|LostCAN|LostIMU|LostLidar|LostLocalization|LostRGBD|WheelErrorLeft|WheelErrorRight)", examples=[0, 1, -1]),
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        
        encoded_params = clean_and_encode_params({
            "start_time": start_time, 
            "end_time": end_time, 
            "shop_id": shop_id, 
            "offset": offset, 
            "limit": limit, 
            "error_levels": error_levels, 
            "error_types": error_types, 
            "timezone_offset": timezone_offset
        })
        
        try:
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/log/error/query_list?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/shops/robot-charges", response_model=RobotChargeResponse, responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": shops_robotcharges_example
            }
        }
    },
})
def get_shops_robot_charges(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1), 
        timezone_offset: int = 0,
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        
        encoded_params = clean_and_encode_params({
            "start_time": start_time, 
            "end_time": end_time, 
            "shop_id": shop_id, 
            "offset": offset, 
            "limit": limit, 
            "timezone_offset": timezone_offset
        })
        
        try:
            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/log/charge/query_list?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}


# Commented out because of PUDU Timeout
# @router.get("/shops/robot-battery", response_model=RobotBatteryResponse)
# def get_shops_robot_changes(
    #     start_time: int = Query(description="Unix timestamp", ge=0),
    #     end_time: int = Query(description="Unix timestamp", ge=0),
    #     shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
    #     offset: int = Query(0, ge=0),
    #     limit: int = Query(10, ge=1), 
    #     timezone_offset: int = 0,
    #     sn: str | None = Query(None, description="Robot Serial Number"),
    #     min_cycle: int | None = Query(None, description="Minimum cycle count (filter active when ≥0)", ge=0),
    #     max_cycle: int | None = Query(None, description="Maximum cycle count (filter active when ≥0)", ge=0),
    #     min_full_capacity: int | None = Query(None, description="Minimum full capacity (filter active when ≥0)", ge=0),
    #     max_full_capacity: int | None = Query(None, description="Maximum full capacity (filter active when ≥0)", ge=0),
    # ):
    #     encoded_params = clean_and_encode_params({
    #         "start_time": start_time, 
    #         "end_time": end_time, 
    #         "shop_id": shop_id, 
    #         "offset": offset, 
    #         "limit": limit, 
    #         "timezone_offset": timezone_offset,
    #         "sn": sn,
    #         "min_cycle": min_cycle,
    #         "max_cycle": max_cycle,
    #         "min_full_capacity": min_full_capacity,
    #         "max_full_capacity": max_full_capacity
    #     })
        
    #     try:
    #         request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/log/battery/query_list?{encoded_params}')
    #         hmac_headers = build_headers_with_hmac(**request_data)
    #         response = requests.get(request_data["url"], headers=hmac_headers)
                
    #         if response.status_code == 200:
    #             return response.json()
    #         else:
    #             return { "code": response.status_code, "message": response.text}
    #     except Exception as e:
    #         return {"status": "ERROR", "message": str(e)}