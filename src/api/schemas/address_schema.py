from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from typing import Optional, Annotated
from pydantic import constr, field_validator
from ..utils import validate_zip_code

class AddressRequestSchema(BaseRequestSchema):
    type: str
    street: str
    number: str
    neighborhood: str
    city: str
    state: Annotated[str, constr(min_length=2, max_length=2)]
    complement: Optional[str] = None
    zip_code: str

    @field_validator('zip_code', mode='before')
    def validate_zip_code(cls, value):
        if not validate_zip_code(value):
            raise ValueError(f"Invalid zip code: {value}")
        return value

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