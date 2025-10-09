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
    return {
        "chart": [
        {
            "task_time": "2023-09-01",
            "run_count": 1,
            "list": [
            {
                "task_time": "2023-09-01",
                "product_code": "67",
                "run_count": 1
            }
            ]
        },
        {
            "task_time": "2023-09-02",
            "run_count": 0,
            "list": []
        }
        ],
        "qoq_chart": [
        {
            "task_time": "2023-08-30",
            "run_count": 1,
            "list": [
            {
                "task_time": "2023-08-30",
                "product_code": "67",
                "run_count": 1
            }
            ]
        },
        {
            "task_time": "2023-08-31",
            "run_count": 3,
            "list": [
            {
                "task_time": "2023-08-31",
                "product_code": "67",
                "run_count": 2
            },
            {
                "task_time": "2023-08-31",
                "product_code": "61",
                "run_count": 1
            }
            ]
        }
        ]
  }

def generate_robot_statistics_example_data() :
    # Mock data to remove
    return {
        "summary": {
            "boot_count": 0,
            "total_count": 3,
            "bind_count": 3,
            "active_count": 2,
            "lively_rate": 0
        },
        "qoq": {
            "boot_count": 0,
            "total_count": 2,
            "bind_count": 0,
            "active_count": 0,
            "lively_rate": 0
        },
        "chart": {
            "61": {
                "product_code": "61",
                "bind_count": 1,
                "active_count": 1,
                "bind_rate": 33.33,
                "active_rate": 50
            },
            "62": {
                "product_code": "62",
                "bind_count": 2,
                "active_count": 1,
                "bind_rate": 66.67,
                "active_rate": 50
            }
        }
    }

@router.get("/robots", response_model=RobotListResponse)
def get_robots(limit: int = 10, offset: int = 0, shop_id: int = None):
    # Mock data to remove - change it to PUDU-API-Call
    robotList = generate_robot_example_data()

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
    data = generate_robot_analysis_example_data()

    return RobotAnalysisResponse(
        data = data,
        message = "ok",
        trace_id = "###ABC###"
    )

@router.get("/robots/statistics", response_model=RobotStatisticsResponse)
def get_robot_statistics(start_time: int, end_time: int, shop_id: int = None, timezone_offset: int = 0):
    # Mock data to remove - change it to PUDU-API-Call
    data = generate_robot_analysis_example_data()

    return RobotStatisticsResponse(
        data = data,
        message = "ok",
        trace_id = "###ABC###"
    )



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
