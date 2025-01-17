from .base_schema import BaseModelSchema
from datetime import date
from typing import Optional

class ContractSchema(BaseModelSchema):
    client_id: int
    sei_id: Optional[int] = None
    contract_number: str
    admin_process_number: str
    total_employees: Optional[int] = None
    start_date: date
    end_date: date
    total_contract_value: float
    monthly_contract_value: float
    execution_date: Optional[date] = None
    adjustment_date: Optional[date] = None
    extension_description: Optional[str] = None
    extension_date: Optional[date] = None