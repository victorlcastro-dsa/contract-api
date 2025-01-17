from .base_schema import BaseModelSchema
from typing import Optional

class OrganizationClientSchema(BaseModelSchema):
    address_id: int
    company_name: str
    uasg: Optional[str] = None
    trade_name: Optional[str] = None
    cnpj: str