from typing import Type, TypeVar, List, Optional
from tortoise.models import Model
from .interfaces.base_repository_interface import BaseRepositoryInterface

T = TypeVar('T', bound=Model)

class BaseRepository(BaseRepositoryInterface[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def get_by_id(self, id: int) -> Optional[T]:
        return await self.model.filter(id=id).first()

    async def get_all(self) -> List[T]:
        return await self.model.all()

    async def create(self, entity: T) -> T:
        await entity.save()
        return entity

    async def update(self, id: int, **kwargs) -> Optional[T]:
        await self.model.filter(id=id).update(**kwargs)
        return await self.get_by_id(id)

    async def delete(self, id: int) -> bool:
        deleted_count = await self.model.filter(id=id).delete()
        return deleted_count > 0