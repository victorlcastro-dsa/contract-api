from tortoise import Tortoise, run_async
from src.api.database.config import Config

async def init_db():
    await Tortoise.init(
        db_url=Config.DATABASE_URL,
        modules={'models': ['src.api.models']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()