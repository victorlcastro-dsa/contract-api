from tortoise import fields
from .base_model import BaseModel
from tortoise.signals import pre_save
from dateutil.relativedelta import relativedelta
from tortoise import Tortoise

class Contract(BaseModel):
    client = fields.ForeignKeyField("models.OrganizationClient", related_name="contracts")
    sei = fields.ForeignKeyField("models.Sei", related_name="contracts", null=True)
    contract_number = fields.CharField(max_length=100, unique=True)
    admin_process_number = fields.CharField(max_length=100)
    total_employees = fields.IntField(null=True)
    start_date = fields.DateField()
    end_date = fields.DateField()
    total_contract_value = fields.DecimalField(max_digits=15, decimal_places=2)
    monthly_contract_value = fields.DecimalField(max_digits=15, decimal_places=2)
    execution_date = fields.DateField(null=True)
    adjustment_date = fields.DateField(null=True)  # Start date + 12 months
    extension_description = fields.TextField(null=True)
    extension_date = fields.DateField(null=True)

    class Meta:
        table = "contracts"

@pre_save(Contract)
async def set_adjustment_date(sender, instance, using_db, update_fields):
    if instance.start_date and not instance.adjustment_date:
        instance.adjustment_date = instance.start_date + relativedelta(months=12)