from .base_model import BaseModel
from tortoise import fields
from quart_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Sei(BaseModel):
    login = fields.CharField(max_length=255)
    password_hash = fields.CharField(max_length=255)
    url = fields.CharField(max_length=500)

    class Meta:
        table = "sei"
        unique_together = ("login", "url")

    @classmethod
    def create_password_hash(cls, password: str) -> str:
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)