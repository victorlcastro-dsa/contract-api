from tortoise import fields
from .base_model import BaseModel

class Role(BaseModel):
    contract = fields.ForeignKeyField("models.Contract", related_name="roles")
    union = fields.ForeignKeyField("models.Union", related_name="roles")
    address = fields.ForeignKeyField("models.Address", related_name="roles", null=True)
    role_name = fields.CharField(max_length=255)
    quantity = fields.IntField()
    base_salary = fields.DecimalField(max_digits=15, decimal_places=2)
    monthly_hours = fields.FloatField()
    weekly_hours = fields.FloatField()
    daily_hours = fields.FloatField()
    hourly_salary = fields.DecimalField(max_digits=15, decimal_places=2)
    contractual_salary = fields.DecimalField(max_digits=15, decimal_places=2)
    education_level = fields.CharField(max_length=255)
    requirements = fields.TextField(null=True)
    exams = fields.TextField(null=True)
    base_date = fields.DateField(null=True)

    class Meta:
        table = "roles"