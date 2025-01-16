from tortoise import fields
from .base_model import BaseModel

class Item(BaseModel):
    general_info = fields.ForeignKeyField("models.GeneralInformation", related_name="items")
    item_type = fields.CharField(max_length=255)  # Type (Uniform, PPE, etc.)
    item_name = fields.CharField(max_length=255)
    quantity = fields.IntField()
    description = fields.TextField(null=True)
    frequency = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "items"