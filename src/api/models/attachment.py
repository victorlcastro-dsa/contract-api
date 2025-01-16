from tortoise import fields
from .base_model import BaseModel

class Attachment(BaseModel):
    contract = fields.ForeignKeyField("models.Contract", related_name="attachments")
    version = fields.CharField(max_length=50, null=True)
    number = fields.CharField(max_length=50)
    expiration_date = fields.DateField(null=True)
    description = fields.TextField(null=True)
    observation = fields.TextField(null=True)
    request_date = fields.DateField(null=True)
    update_date = fields.DateField(null=True)
    url = fields.CharField(max_length=500, unique=True)

    class Meta:
        table = "attachments"