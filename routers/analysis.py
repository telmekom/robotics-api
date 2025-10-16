from fastapi import Query, APIRouter
import requests
from schemas.analysis import *
from schemas.shop import *
from schemas.statistics import RobotOpsStatisticsResponse, RobotStatisticsResponse, ShopStatisticsResponse
from shared.pudu_api_helper import build_headers_with_hmac, clean_and_encode_params, generate_get_header_block
from shared.time import TimeUnit
import os
from dotenv import load_dotenv
load_dotenv()  

router = APIRouter(
    tags=["Statistics & Analysis"],
)

### ANALYSIS ENDPOINTS ###

@router.get("/analysis/shops/general",  response_model=AnalysisResponse, name="PUDU-Annotation: Store analytics")
def get_analysis_shops_general(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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
            return {"code": "UKN", "message": str(e)}

@router.get("/analysis/shops/cleaning/detail", response_model=AnalysisResponse, name="PUDU-Annotation: Machine Task Analysis [Cleaning Line] - Cleaning Mode Working Session Distribution")
def get_analysis_shops_cleaning_detail(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
        time_unit: TimeUnit = Query(TimeUnit.DAY, description="Granularity of the charts", examples=[TimeUnit.DAY, TimeUnit.HOUR]),
        clean_mode: int = Query(0, description="Clean Mode (0: all, 1: scrubber, 2: sweeping)", ge=0, le=2),
        sub_mode: int = Query(0, description="Sub Clean Mode (-1: all, 0: custom, 1: carpet vacuuming, 3: silent dust pushing)", ge=0, le=3),
        timezone_offset: int = 0
    ):
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset,
                "clean_mode": clean_mode,
                "sub_mode": sub_mode,
                "time_unit": time_unit.value
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/clean/detail?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/analysis/shops/cleaning", response_model=AnalysisResponse, name="PUDU-Annotation: Machine Task Analysis [Cleaning Line] - Cleaning Mode")
def get_analysis_shops_cleaning(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0),  
        time_unit: TimeUnit = Query(TimeUnit.DAY, description="Granularity of the charts", examples=[TimeUnit.DAY, TimeUnit.HOUR]),
        clean_mode: int = Query(0, description="Clean Mode (0: all, 1: scrubber, 2: sweeping)", ge=0, le=2),
        sub_mode: int = Query(0, description="Sub Clean Mode (-1: all, 0: custom, 1: carpet vacuuming, 3: silent dust pushing)", ge=0, le=3),
        timezone_offset: int = 0
    ):
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset,
                "clean_mode": clean_mode,
                "sub_mode": sub_mode,
                "time_unit": time_unit.value
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/clean/mode?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
        
@router.get("/analysis/shops/industrial", response_model=AnalysisResponse, name="PUDU-Annotation: Machine Task Analysis[Industrial Line] - Jacking Mode")
def get_analysis_shops_industrial(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/lifting?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
   
@router.get("/analysis/shops/delivery", response_model=AnalysisResponse, name="PUDU-Annotation: Machine task analysis [distribution line] - distribution mode")
def get_analysis_shops_delivery(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0),  
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/delivery?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/cruise", response_model=AnalysisResponse, name="PUDU-Annotation: Machine Mission Analysis [Distribution Line] - Cruise Mode")
def get_analysis_shops_cruise(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/cruise?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/lead", response_model=AnalysisResponse, name="PUDU-Annotation: Machine Mission Analysis [Distribution Line] - Lead Mode")
def get_analysis_shops_lead(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/greeter?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/interactive", response_model=AnalysisResponse, name="PUDU-Annotation: Machine task analysis [distribution line] - interactive mode")
def get_analysis_shops_interactive(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/interactive?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/solicit", response_model=AnalysisResponse, name="PUDU-Annotation: Machine task analysis [distribution line] - customer collection mode")
def get_analysis_shops_solicit(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/solicit?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/grid", response_model=AnalysisResponse, name="PUDU-Annotation: Machine task analysis [distribution line] - grid click")
def get_analysis_shops_grid(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/grid?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/ad", response_model=AnalysisResponse, name="PUDU-Annotation: Machine task analysis [distribution line] - grid click")
def get_analysis_shops_ad(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
        time_unit: TimeUnit = Query(TimeUnit.DAY, description="Granularity of the charts", examples=[TimeUnit.DAY, TimeUnit.HOUR]),
        timezone_offset: int = 0,
        ad_id: int | None = Query(None, description="If left empty it will return data for all ads", ge=0)
    ):
        try:
            encoded_params = clean_and_encode_params({
                "start_time": start_time, 
                "end_time": end_time, 
                "shop_id": shop_id, 
                "timezone_offset": timezone_offset,
                "time_unit": time_unit.value,
                "ad_id": ad_id
            })

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/ad?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}
  
@router.get("/analysis/shops/call", response_model=AnalysisResponse, name="PUDU-Annotation: Machine Task Analysis [distribution Line] - Call Pattern")
def get_analysis_shops_grid(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

            request_data = generate_get_header_block(f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-board/v1/analysis/task/call?{encoded_params}')
            hmac_headers = build_headers_with_hmac(**request_data)
            response = requests.get(request_data["url"], headers=hmac_headers)
                
            if response.status_code == 200:
                return response.json()
            else:
                return { "code": response.status_code, "message": response.text}
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

@router.get("/analysis/robot/general", response_model=AnalysisResponse, name="PUDU-Annotation: Machine run analysis")
def get_analysis_robot_general(start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

### STATISTICS ENDPOINTS ###

@router.get("/statistics/shops/general", response_model=ShopStatisticsResponse, name="PUDU-Annotation: Store overview")
def get_statistics_shops_general(
        start_time: int = Query(description="Unix timestamp", ge=0),
        end_time: int = Query(description="Unix timestamp", ge=0),
        shop_id: int | None = Query(None, description="If left empty it will return data for all shops", ge=0), 
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

@router.get("/statistics/robots/general", response_model=RobotStatisticsResponse, name="PUDU-Annotation: Overview of the machine")
def get_statistics_robots_general(
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
        
@router.get("/statistics/robots/operations", response_model=RobotOpsStatisticsResponse, name="PUDU-Annotation: Overview of machine operation")
def get_statistics_robots_operations(
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