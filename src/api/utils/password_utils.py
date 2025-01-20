from quart_bcrypt import Bcrypt
from .response import ResponseHandler

bcrypt = Bcrypt()

def create_password_hash(password: str) -> str:
    try:
        return bcrypt.generate_password_hash(password).decode('utf-8')
    except Exception as e:
        return ResponseHandler.exception(e)

def check_password(password_hash: str, password: str) -> bool:
    try:
        return bcrypt.check_password_hash(password_hash, password)
    except Exception as e:
        return ResponseHandler.exception(e)