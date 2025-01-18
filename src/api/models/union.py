from .base_model import BaseModel
from tortoise import fields

class Union(BaseModel):
    name = fields.CharField(max_length=255)
    cnpj = fields.CharField(max_length=18, unique=True)

    class Meta:
        table = "unions"