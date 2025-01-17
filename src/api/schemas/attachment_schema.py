from .base_schema import BaseRequestSchema, BaseResponseSchema
from datetime import date
from typing import Optional

class AttachmentRequestSchema(BaseRequestSchema):
    contract_id: int
    version: Optional[str] = None
    number: str
    expiration_date: Optional[date] = None
    description: Optional[str] = None
    observation: Optional[str] = None
    request_date: Optional[date] = None
    update_date: Optional[date] = None
    url: str

class AttachmentResponseSchema(BaseResponseSchema):
    contract_id: int
    version: Optional[str] = None
    number: str
    expiration_date: Optional[date] = None
    description: Optional[str] = None
    observation: Optional[str] = None
    request_date: Optional[date] = None
    update_date: Optional[date] = None
    url: str