from pydantic import BaseModel, Field
from typing import List, Optional

class SearchQueryParser(BaseModel):
    """
    用于解析用户购物查询的数据结构。
    """
    product_name: str = Field(description="用户想要购买的核心产品名称, 例如 '机械键盘' 或 '咖啡机'")
    features: List[str] = Field(description="用户提到的所有具体特性、属性或要求, 例如 ['安静', '87键', '新手']")
    budget: Optional[int] = Field(description="用户的预算金额，如果提到的话")
    raw_query: str = Field(description="用户的原始查询字符串")