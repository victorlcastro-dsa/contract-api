from .base_schema import BaseModelSchema
from typing import Optional

class ItemSchema(BaseModelSchema):
    general_info_id: int
    item_type: str
    item_name: str
    quantity: int
    description: Optional[str] = None
    frequency: Optional[str] = None