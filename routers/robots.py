from fastapi import Depends, Query, APIRouter
from schemas.robot import *
from shared.time import TimeUnit

router = APIRouter(
    tags=["Robots"],
    responses={404: {"description": "Robots API for Data, Analytics and Statistics"}}
)

def generate_robot_example_data() :
    # Mock data to remove
    return [
            {
                "mac": "20:50:E7:3E:61:78",
                "shop_id": "324100000",
                "shop_name": "【10月08日】出尘门店",
                "sn": "OP2023090702",
                 "product_code":"PuduBot"
            },
            {
                "mac": "B4:ED:D5:75:6E:E8",
                "shop_id": "324100000",
                "shop_name": "【10月08日】出尘门店",
                "sn": "8110A3802050003",
                 "product_code":"PuduBot"
            }
        ]

def generate_robot_analysis_example_data() :
    # Mock data to remove
    return {}

@router.get("/robots", response_model=RobotListResponse)
def get_robots(limit: int = 10, offset: int = 0, shop_id: int = None):
    # Mock data to remove - change it to PUDU-API-Call
    robotList : List[RobotListItem] = generate_robot_example_data()

    return RobotListResponse(
        data = {
            "count": len(robotList),
            "list": robotList
        },
        message = "ok",
        trace_id = "###ABC###"
    )

@router.get("/robots/analysis", response_model=RobotAnalysisResponse)
def get_robot_analysis(start_time: int, end_time: int, shop_id: int = None, time_unit: TimeUnit = TimeUnit.DAY, timezone_offset: int = 0):
    # Mock data to remove - change it to PUDU-API-Call
    data = generate_robot_analysis_example_data

    return RobotListResponse(
        data = data,
        message = "ok",
        trace_id = "###ABC###"
    )





# TODO
@router.get("/robots/statistics", response_model=None)
def get_robot_statistics(limit: int = 10, offset: int = 0, shop_id: int = None):
    # Mock data to remove - change it to PUDU-API-Call
    data = []

    return None

# TODO
@router.get("/robot-ops/analysis ", response_model=None)
def get_robot_ops_analysis(limit: int = 10, offset: int = 0, shop_id: int = None):
    # Mock data to remove - change it to PUDU-API-Call
    data = []

    return None

# TODO
@router.get("/robot-ops/statistics ", response_model=None)
def get_robot_ops_statistics(limit: int = 10, offset: int = 0, shop_id: int = None):
    # Mock data to remove - change it to PUDU-API-Call
    data = []

    return None
