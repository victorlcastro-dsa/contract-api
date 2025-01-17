from .base_schema import BaseModelSchema
from typing import Optional

class AddressSchema(BaseModelSchema):
    id: int
    type: str
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    complement: Optional[str] = None
    zip_code: str
