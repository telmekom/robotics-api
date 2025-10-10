from fastapi import Depends, Query, APIRouter
import requests
from schemas.shop import *
from shared.pudu_api_helper import build_headers_with_hmac
from shared.time import TimeUnit
from urllib.parse import urlencode
import os
from dotenv import load_dotenv
load_dotenv()  

router = APIRouter(
    tags=["Shops"],
    responses={404: {"description": "Shops API for Data, Analytics and Statistics"}}
)

@router.get("/shops", response_model=ShopListResponse)
def get_shops(limit: int = 10, offset: int = 0):
        try:
            request_data = {
                "url": f'{os.getenv("PUDU_API_URL")}/api/shop?limit={limit}&offset={offset}',
                "accept": 'application/json',
                "content_type": 'application/json',
                "method": 'GET',
                "app_key" : os.getenv("API_APP_KEY"),
                "secret_key": os.getenv("API_APP_SECRET"),
            }
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                # [TODO] better error info
                return { response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/shops/statistics", response_model=ShopStatisticsResponse)
def get_shop_statistics(start_time: int, end_time: int, shop_id: int = None, timezone_offset: int = 0):
    try:
        params = {
            "start_time": start_time, 
            "end_time": end_time, 
            "shop_id": shop_id, 
            "timezone_offset": timezone_offset
        }
        params = {k: v for k, v in params.items() if v is not None}
        params = dict(sorted(params.items()))
        encoded_params = urlencode(params)


        request_data = {
            "url": f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/brief/shop?{encoded_params}',
            "accept": 'application/json',
            "content_type": 'application/json',
            "method": 'GET',
            "app_key" : os.getenv("API_APP_KEY"),
            "secret_key": os.getenv("API_APP_SECRET"),
        }

        hmac_headers = build_headers_with_hmac(**request_data)
        response = requests.get(request_data["url"], headers=hmac_headers)
            
        if response.status_code == 200:
            return response.json()
        else:
            # [TODO] better error info
            return { response.text}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}


@router.get("/shops/analysis")
def get_shop_analytics(start_time: int, end_time: int, shop_id: int = None, time_unit: TimeUnit = TimeUnit.DAY, timezone_offset: int = 0):
    try:
        params = {
            "start_time": start_time, 
            "end_time": end_time, 
            "shop_id": shop_id, 
            "timezone_offset": timezone_offset,
            "time_unit": time_unit.value
        }
        params = {k: v for k, v in params.items() if v is not None}
        params = dict(sorted(params.items()))
        encoded_params = urlencode(params)


        request_data = {
            "url": f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/shop?{encoded_params}',
            "accept": 'application/json',
            "content_type": 'application/json',
            "method": 'GET',
            "app_key" : os.getenv("API_APP_KEY"),
            "secret_key": os.getenv("API_APP_SECRET"),
        }

        hmac_headers = build_headers_with_hmac(**request_data)
        response = requests.get(request_data["url"], headers=hmac_headers)
            
        if response.status_code == 200:
            return response.json()
        else:
            # [TODO] better error info
            return { response.text}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}
