from tortoise import fields
from .base_model import BaseModel
from ..utils.validators import validate_zip_code

class Address(BaseModel):
    type = fields.CharField(max_length=50)
    street = fields.CharField(max_length=255)
    number = fields.CharField(max_length=10)
    neighborhood = fields.CharField(max_length=255)
    city = fields.CharField(max_length=255)
    state = fields.CharField(max_length=2)
    complement = fields.TextField(null=True)
    zip_code = fields.CharField(max_length=15, validators=[validate_zip_code])

    class Meta:
        unique_together = (
            "type",
            "street",
            "number",
            "neighborhood",
            "city",
            "state",
            "complement",
            "zip_code",
        )