from tortoise import Tortoise
from src.api.database.config import TORTOISE_ORM

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    async def init_db(self):
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()

    async def close_db(self):
        await Tortoise.close_connections()