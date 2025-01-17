from .base_schema import BaseModelSchema

class UnionSchema(BaseModelSchema):
    name: str
    cnpj: str