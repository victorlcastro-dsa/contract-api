from tortoise import fields
from .base_model import BaseModel
from ..utils import validate_cnpj

class OrganizationClient(BaseModel):
    address = fields.ForeignKeyField("models.Address", related_name="clients")
    company_name = fields.CharField(max_length=255)
    uasg = fields.CharField(max_length=50, null=True)
    trade_name = fields.CharField(max_length=255, null=True)
    cnpj = fields.CharField(max_length=20, unique=True, validators=[validate_cnpj])

    class Meta:
        table = "organization_clients"