from tortoise import fields
from .base_model import BaseModel

class Contact(BaseModel):
    role = fields.ForeignKeyField("models.Role", related_name="contacts")
    department = fields.CharField(max_length=255, null=True)
    name = fields.CharField(max_length=255)
    residence_number = fields.CharField(max_length=20, null=True)
    whatsapp_number = fields.CharField(max_length=20, null=True)
    email = fields.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ("role", "department", "name", "residence_number", "whatsapp_number", "email")