from .base_model import BaseModel
from tortoise import fields
from ..utils import create_password_hash

class Sei(BaseModel):
    login = fields.CharField(max_length=255)
    password_hash = fields.CharField(max_length=255)
    url = fields.CharField(max_length=500)

    class Meta:
        table = "sei"
        unique_together = ("login", "url")

    async def save(self, *args, **kwargs):
        if not self.password_hash.startswith('$2b$'):
            self.password_hash = create_password_hash(self.password_hash)
        await super().save(*args, **kwargs)