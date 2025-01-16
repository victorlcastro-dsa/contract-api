from tortoise import Tortoise, run_async

async def init_db():
    await Tortoise.init(
        db_url='postgres://user:password@db:5432/contract_db',
        modules={'models': ['src.api.models']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()