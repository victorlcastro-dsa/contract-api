from .base_schema import BaseRequestSchema, BaseResponseSchema

class UnionRequestSchema(BaseRequestSchema):
    name: str
    cnpj: str

class UnionResponseSchema(BaseResponseSchema):
    name: str
    cnpj: str