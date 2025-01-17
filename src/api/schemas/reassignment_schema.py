from .base_schema import BaseRequestSchema, BaseResponseSchema
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