from .base_schema import BaseModelSchema
from datetime import date
from typing import Optional

class AttachmentSchema(BaseModelSchema):
    contract_id: int
    version: Optional[str] = None
    number: str
    expiration_date: Optional[date] = None
    description: Optional[str] = None
    observation: Optional[str] = None
    request_date: Optional[date] = None
    update_date: Optional[date] = None
    url: str