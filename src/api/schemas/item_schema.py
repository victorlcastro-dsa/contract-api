from .base_schema import BaseRequestSchema, BaseResponseSchema
from typing import Optional

class ItemRequestSchema(BaseRequestSchema):
    general_info_id: int
    item_type: str
    item_name: str
    quantity: int
    description: Optional[str] = None
    frequency: Optional[str] = None

class ItemResponseSchema(BaseResponseSchema):
    general_info_id: int
    item_type: str
    item_name: str
    quantity: int
    description: Optional[str] = None
    frequency: Optional[str] = None