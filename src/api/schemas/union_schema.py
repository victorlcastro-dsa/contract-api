from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from pydantic import field_validator
from ..utils import validate_cnpj

class UnionRequestSchema(BaseRequestSchema):
    name: str
    cnpj: str

    @field_validator('cnpj', mode='before')
    def validate_cnpj(cls, value):
        if not validate_cnpj(value):
            raise ValueError(f"Invalid CNPJ: {value}")
        return value

class UnionResponseSchema(BaseResponseSchema):
    name: str
    cnpj: str

class UnionListResponseSchema(BaseListResponseSchema[UnionResponseSchema]):
    pass