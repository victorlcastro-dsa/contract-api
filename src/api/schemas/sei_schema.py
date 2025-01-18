from .base_schema import BaseRequestSchema,BaseResponseSchema, BaseListResponseSchema

class SeiRequestSchema(BaseRequestSchema):
    login: str
    password_hash: str
    url: str

class SeiResponseSchema(BaseResponseSchema):
    login: str
    password_hash: str
    url: str

class SeiListResponseSchema(BaseListResponseSchema[SeiResponseSchema]):
    pass