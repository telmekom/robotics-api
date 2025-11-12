from fastapi import Depends, Query, APIRouter
import requests
from schemas.maps import MapDetailsResponse, MapListResponse
from shared.pudu_api_helper import HACKATHON_API_KEY, EntityType, build_headers_with_hmac, clean_and_encode_params, generate_get_header_block, header_scheme, is_allowed_id, run_url
import os
from dotenv import load_dotenv
from examples.maps import maps_example, maps_detail_example
load_dotenv()  

router = APIRouter(
    tags=["Maps"],
)

@router.get("/maps", response_model=MapListResponse, name="Map List", description="", responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": maps_example
            }
        }
    },
})
def get_maps(
        shop_id: int = Query(description="Parent Shop ID"),
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
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

@router.get("/maps/details", name="Map Details", response_model=MapDetailsResponse, description="", responses={
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": maps_detail_example
            }
        }
    },
})
def get_map_detail(
        shop_id: int = Query(description="Parent Shop ID"),
        map_name: str = Query(description="Map Name - used as Identifier"),
        device_width: int = Query(1200, description="Device width in px", gt=0),
        device_height: int = Query(800, description="Device height in px", gt=0),
        key: str = Depends(header_scheme)
    ):
        if (key != HACKATHON_API_KEY):
            return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        if not is_allowed_id(EntityType.SHOP, str(shop_id)):
             return {"code": 403, "message": "Forbidden: Shop ID not whitelisted"}
        
        try:
            encoded_params = clean_and_encode_params({
                "shop_id": shop_id, 
                "map_name": map_name,
                "device_width": device_width, 
                "device_height": device_height,
            })            

            url = f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-open-platform-service/v1/api/map?{encoded_params}'
            response = run_url(url, os.getenv("API_APP_KEY"), os.getenv("API_APP_SECRET"))
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

