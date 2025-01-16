from tortoise import fields
from .base_model import BaseModel
from .item import Item

class GeneralInformation(BaseModel):
    contract = fields.ForeignKeyField("models.Contract", related_name="general_information", unique=True)
    supervision = fields.BooleanField(default=False)
    supervision_frequency = fields.CharField(max_length=255, null=True)
    supervision_description = fields.TextField(null=True)
    technical_reports = fields.BooleanField(default=False)
    technical_reports_frequency = fields.CharField(max_length=255, null=True)
    billing_documents = fields.TextField(null=True)
    client_documents = fields.TextField(null=True)
    pre_start_date = fields.DateField(null=True)
    start_date = fields.DateField(null=True)
    monthly_date = fields.DateField(null=True)
    quarterly_date = fields.DateField(null=True)
    biannual_date = fields.DateField(null=True)
    yearly_date = fields.DateField(null=True)
    near_office = fields.BooleanField(default=False)
    office_city = fields.CharField(max_length=255, null=True)
    contractual_guarantee = fields.BooleanField(default=False)
    guarantee_percentage = fields.FloatField(null=True)
    items = fields.ReverseRelation["Item"]

    class Meta:
        table = "general_information"