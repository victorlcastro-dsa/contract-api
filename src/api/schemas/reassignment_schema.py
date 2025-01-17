from .base_schema import BaseModelSchema
from datetime import date

class ReassignmentSchema(BaseModelSchema):
    role_id: int
    insalubrity: bool
    insalubrity_date: date
    reassignment_union_date: date