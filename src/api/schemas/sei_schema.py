from .base_schema import BaseRequestSchema,BaseResponseSchema

class SeiRequestSchema(BaseRequestSchema):
    login: str
    password_hash: str
    url: str

class SeiResponseSchema(BaseResponseSchema):
    login: str
    password_hash: str
    url: str