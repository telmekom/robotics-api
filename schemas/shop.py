from typing import List, Union
from pydantic import BaseModel

from schemas.base import BaseResponse

# Shop List

class Shop(BaseModel):
    company_id: int
    company_name: str
    shop_id: int
    shop_name: str

class ShopListData(BaseModel):
    count: int
    list: List[Shop]

class ShopListResponse(BaseResponse):
    data: ShopListData
