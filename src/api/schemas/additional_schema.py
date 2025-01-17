from .base_schema import BaseModelSchema
from datetime import date
from typing import Optional

class AdditionalSchema(BaseModelSchema):
    role_id: int
    type: str
    boolean_value: Optional[bool] = None
    numeric_value: Optional[float] = None
    percentage: Optional[float] = None
    description: Optional[str] = None
    base_date: Optional[date] = None