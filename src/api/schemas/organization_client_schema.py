from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from typing import Optional
from pydantic import field_validator
from ..utils import validate_cnpj

class OrganizationClientRequestSchema(BaseRequestSchema):
    address_id: int
    company_name: str
    uasg: Optional[str] = None
    trade_name: Optional[str] = None
    cnpj: str

    @field_validator('cnpj', mode='before')
    def validate_cnpj(cls, value):
        if not validate_cnpj(value):
            raise ValueError(f"Invalid CNPJ: {value}")
        return value

class OrganizationClientResponseSchema(BaseResponseSchema):
    address_id: int
    company_name: str
    uasg: Optional[str] = None
    trade_name: Optional[str] = None
    cnpj: str

class OrganizationClientListResponseSchema(BaseListResponseSchema[OrganizationClientResponseSchema]):
    pass