from .base_schema import BaseModelSchema
from pydantic import EmailStr
from typing import Optional

class ContactSchema(BaseModelSchema):
    role_id: int
    department: Optional[str] = None
    name: str
    residence_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    email: Optional[EmailStr] = None