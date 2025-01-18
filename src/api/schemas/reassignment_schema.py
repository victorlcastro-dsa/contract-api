from .base_schema import BaseRequestSchema, BaseResponseSchema, BaseListResponseSchema
from datetime import date

class ReassignmentRequestSchema(BaseRequestSchema):
    role_id: int
    insalubrity: bool
    insalubrity_date: date
    reassignment_union_date: date

class ReassignmentResponseSchema(BaseResponseSchema):
    role_id: int
    insalubrity: bool
    insalubrity_date: date
    reassignment_union_date: date

class ReassignmentListResponseSchema(BaseListResponseSchema[ReassignmentResponseSchema]):
    pass