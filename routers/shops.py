from fastapi import Query, APIRouter
import requests
from schemas.shop import *
from shared.pudu_api_helper import build_headers_with_hmac, clean_and_encode_params, generate_get_header_block
from shared.time import TimeUnit
import os
from dotenv import load_dotenv
load_dotenv()  

router = APIRouter(
    tags=["Shops"],
    responses={404: {"description": "Shops API for Data, Analytics and Statistics"}}
)

@router.get("/shops", response_model=ShopListResponse)
def get_shops(
        limit: int = Query(10, ge=1), 
        offset: int = Query(0, ge=0)
    ):
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

@router.get("/shops/statistics", response_model=ShopStatisticsResponse)
def get_shop_statistics(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = None,
        timezone_offset: int = Query(0, description="GMT offset (GMT-12 to GMT+14)", ge=-12, le=14),
    ):
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/brief/shop?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}


@router.get("/shops/analysis")
def get_shop_analytics(
        start_time: int = Query(description="Unix timestamp", ge=0),
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/shop?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
