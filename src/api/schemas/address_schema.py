from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from typing import Optional

class AddressRequestSchema(BaseRequestSchema):
    type: str
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    complement: Optional[str] = None
    zip_code: str

class AddressResponseSchema(BaseResponseSchema):
    type: str
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    complement: Optional[str] = None
    zip_code: str

class AddressListResponseSchema(BaseListResponseSchema[AddressResponseSchema]):
    pass