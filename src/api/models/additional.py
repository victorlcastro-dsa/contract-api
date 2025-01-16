from tortoise import fields
from .base_model import BaseModel

class Additional(BaseModel):
    role = fields.ForeignKeyField("models.Role", related_name="additionals")
    type = fields.CharField(max_length=255)
    boolean_value = fields.BooleanField(null=True)
    numeric_value = fields.DecimalField(max_digits=15, decimal_places=2, null=True)
    percentage = fields.FloatField(null=True)
    description = fields.TextField(null=True)
    base_date = fields.DateField(null=True)

    class Meta:
        table = "additionals"