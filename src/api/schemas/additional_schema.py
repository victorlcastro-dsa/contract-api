from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from datetime import date
from typing import Optional

class AdditionalRequestSchema(BaseRequestSchema):
    role_id: int
    type: str
    boolean_value: Optional[bool] = None
    numeric_value: Optional[float] = None
    percentage: Optional[float] = None
    description: Optional[str] = None
    base_date: Optional[date] = None

class AdditionalResponseSchema(BaseResponseSchema):
    role_id: int
    type: str
    boolean_value: Optional[bool] = None
    numeric_value: Optional[float] = None
    percentage: Optional[float] = None
    description: Optional[str] = None
    base_date: Optional[date] = None

class AdditionalListResponseSchema(BaseListResponseSchema[AdditionalResponseSchema]):
    pass