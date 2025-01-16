from tortoise import fields
from .base_model import BaseModel
from datetime import date
from dateutil.relativedelta import relativedelta

class Reassignment(BaseModel):
    role = fields.ForeignKeyField("models.Role", related_name="reassignments")
    insalubrity = fields.BooleanField()
    insalubrity_date = fields.DateField(default=date.today() + relativedelta(years=1))
    reassignment_union_date = fields.DateField()

    class Meta:
        table = "reassignments"