from .base_model import BaseModel
from tortoise import fields
from ..utils import validate_cnpj

class Union(BaseModel):
    name = fields.CharField(max_length=255)
    cnpj = fields.CharField(max_length=18, unique=True, validators=[validate_cnpj])

    class Meta:
        table = "unions"