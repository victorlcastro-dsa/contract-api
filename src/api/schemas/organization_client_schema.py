from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from typing import Optional

class OrganizationClientRequestSchema(BaseRequestSchema):
    address_id: int
    company_name: str
    uasg: Optional[str] = None
    trade_name: Optional[str] = None
    cnpj: str

class OrganizationClientResponseSchema(BaseResponseSchema):
    address_id: int
    company_name: str
    uasg: Optional[str] = None
    trade_name: Optional[str] = None
    cnpj: str

class OrganizationClientListResponseSchema(BaseListResponseSchema[OrganizationClientResponseSchema]):
    pass