from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from pydantic import EmailStr, field_validator
from typing import Optional
from ..utils import validate_phone_number, validate_email_address

class ContactRequestSchema(BaseRequestSchema):
    role_id: int
    department: Optional[str] = None
    name: str
    residence_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    email: Optional[EmailStr] = None

    @field_validator('residence_number', 'whatsapp_number', mode='before')
    def validate_phone(cls, value):
        if value and not validate_phone_number(value):
            raise ValueError(f"Invalid phone number: {value}")
        return value

    @field_validator('email', mode='before')
    def validate_email(cls, value):
        if value and not validate_email_address(value):
            raise ValueError(f"Invalid email address: {value}")
        return value

class ContactResponseSchema(BaseResponseSchema):
    role_id: int
    department: Optional[str] = None
    name: str
    residence_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    email: Optional[EmailStr] = None

class ContactListResponseSchema(BaseListResponseSchema[ContactResponseSchema]):
    pass