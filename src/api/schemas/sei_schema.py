from .base_schema import BaseModelSchema

class SeiSchema(BaseModelSchema):
    login: str
    password_hash: str
    url: str