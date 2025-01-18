from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from pydantic import EmailStr
from typing import Optional

class ContactRequestSchema(BaseRequestSchema):
    role_id: int
    department: Optional[str] = None
    name: str
    residence_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    email: Optional[EmailStr] = None

class ContactResponseSchema(BaseResponseSchema):
    role_id: int
    department: Optional[str] = None
    name: str
    residence_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    email: Optional[EmailStr] = None

class ContactListResponseSchema(BaseListResponseSchema[ContactResponseSchema]):
    pass