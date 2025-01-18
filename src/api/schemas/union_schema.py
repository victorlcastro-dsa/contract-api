from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema

class UnionRequestSchema(BaseRequestSchema):
    name: str
    cnpj: str

class UnionResponseSchema(BaseResponseSchema):
    name: str
    cnpj: str

class UnionListResponseSchema(BaseListResponseSchema[UnionResponseSchema]):
    pass