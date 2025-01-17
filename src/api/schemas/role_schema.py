from .base_schema import BaseModelSchema
from datetime import date
from typing import Optional

class RoleSchema(BaseModelSchema):
    contract_id: int
    union_id: int
    address_id: Optional[int] = None
    role_name: str
    quantity: int
    base_salary: float
    monthly_hours: float
    weekly_hours: float
    daily_hours: float
    hourly_salary: float
    contractual_salary: float
    education_level: str
    requirements: Optional[str] = None
    exams: Optional[str] = None
    base_date: Optional[date] = None