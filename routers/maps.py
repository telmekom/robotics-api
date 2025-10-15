import re
import urllib.parse
from fastapi import Query, APIRouter
import requests
from schemas.maps import *
from shared.pudu_api_helper import build_headers_with_hmac, clean_and_encode_params, generate_get_header_block
from shared.time import TimeUnit
import os
from dotenv import load_dotenv
load_dotenv()  

router = APIRouter(
    tags=["Maps"],
    responses={404: {"description": "Maps API for Data, Analytics and Statistics"}}
)

@router.get("/maps", response_model=MapListResponse)
def get_maps(
        shop_id: int = Query(description="Parent Shop ID"),
    ):
        try:
            encoded_params = clean_and_encode_params({
                "shop_id": shop_id, 
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-open-platform-service/v1/api/maps?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

# @router.get("/maps/details")
# def get_map_detail(
#         shop_id: int = Query(description="Parent Shop ID"),
#         map_name: str = Query(description="map name"),
#         device_width: int = Query(1200, description="Device width in px", gt=0),
#         device_height: int = Query(800, description="Device height in px", gt=0),
#     ):
#         try:
#             encoded_params = clean_and_encode_params({
#                 "shop_id": shop_id, 
#                 "map_name": map_name,
#                 "device_width": device_width, 
#                 "device_height": device_height,
#             })            

#             request_data = {
#                 "url": f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-open-platform-service/v1/api/map?{encoded_params}',
#                 "accept": 'application/json',
#                 "content_type": 'application/json',
#                 "method": 'GET',
#                 "app_key" : os.getenv("API_APP_KEY"),
#                 "secret_key": os.getenv("API_APP_SECRET"),
#             }
#             print(request_data["url"])


#             hmac_headers = build_headers_with_hmac(**request_data)
#             response = requests.get(request_data["url"], headers=hmac_headers)
                
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 return { "code": response.status_code, "message": response.text}
#         except Exception as e:
#             return {"status": "ERROR", "message": str(e)}

