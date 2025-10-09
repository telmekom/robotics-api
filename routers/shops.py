from fastapi import Depends, Query, APIRouter
from schemas.shop import *
from shared.time import TimeUnit

router = APIRouter(
    tags=["Shops"],
    responses={404: {"description": "Shops API for Data, Analytics and Statistics"}}
)

def generate_shop_example_data() :
    # Mock data to remove
    return [
        Shop(
            company_id = 11223,
            company_name = "Hackathon NOI",
            shop_id = 0,
            shop_name = "Stage 1",
            ),
        Shop(
            company_id = 11223,
            company_name = "Hackathon NOI",
            shop_id = 1,
            shop_name = "Stage 2",
            ),
        Shop(
            company_id = 11223,
            company_name = "Hackathon NOI",
            shop_id = 2,
            shop_name = "Stage 3",
            ),
        Shop(
            company_id = 11223,
            company_name = "Hackathon NOI",
            shop_id = 3,
            shop_name = "Presentation Stage",
            ),
    ]

def generate_shop_analysis_example_data() : 
    # Mock data to remove
    return {
        "summary": {
            "lively_count": 1,
            "silent_count": 0,
            "new_count": 0,
            "total_count": 1
        },
        "qoq": {
            "lively_count": 1,
            "silent_count": 0,
            "new_count": 0,
            "total_count": 1
        },
        "chart": [
            {
                "task_time": "2023-09-01",
                "lively_count": 1,
                "silent_count": 0,
                "new_count": 0,
                "total_count": 1
            },
            {
                "task_time": "2023-09-02",
                "lively_count": 0,
                "silent_count": 1,
                "new_count": 0,
                "total_count": 1
            }
        ],
        "qoq_chart": [
            {
                "task_time": "2023-08-30",
                "lively_count": 1,
                "silent_count": 0,
                "new_count": 0,
                "total_count": 1
            },
            {
                "task_time": "2023-08-31",
                "lively_count": 1,
                "silent_count": 0,
                "new_count": 0,
                "total_count": 1
            }
        ]
    }

def generate_shop_statistics_example_data() : 
    # Mock data to remove
    return {
        "message": "ok",
        "data": {
            "summary": {
                "lively_count": 1,
                "total_count": 1,
                "new_count": 0,
                "lively_rate": 100
            },
            "qoq": {
                "lively_count": 1,
                "total_count": 1,
                "new_count": 0,
                "lively_rate": 0
            },
            "lively_top10": [
                {
                    "shop_id": 1,
                    "shop_name": "Stage 2",
                    "run_count": 1,
                    "bind_count": 4,
                    "duration": 0.89,
                    "stop_duration": 191.11
                }
            ],
            "silent_top10": []
        }
    }


@router.get("/shops", response_model=ShopListResponse)
def get_shops(limit: int = 10, offset: int = 0):
    # Mock data to remove - change it to PUDU-API-Call
    shopList : List[Shop] = generate_shop_example_data()

    return ShopListResponse(
        data = {
            "count": len(shopList),
            "list": shopList
        },
        message = "ok",
        trace_id = "###ABC###"
    )

@router.get("/shops/analysis", response_model=ShopAnalysisResponse)
def get_shop_analytics(start_time: int, end_time: int, shop_id: int = None, time_unit: TimeUnit = TimeUnit.DAY, timezone_offset: int = 0):
    # Mock data to remove - change it to PUDU-API-Call
    shopAnalysisData = generate_shop_analysis_example_data()

    return ShopAnalysisResponse(
        trace_id = "###ABC###",
        message = "ok",
        data = shopAnalysisData
    )

@router.get("/shops/statistics", response_model=ShopStatisticsResponse)
def get_shop_statistics(start_time: int, end_time: int, shop_id: int = None, timezone_offset: int = 0):
    # Mock data to remove - change it to PUDU-API-Call
    shopStatisticsData = generate_shop_statistics_example_data()

    return ShopStatisticsResponse(
        trace_id = "###ABC###",
        data = shopStatisticsData
    )