from typing import Type, TypeVar, List, Optional
from tortoise.models import Model
from .interfaces.base_repository_interface import BaseRepositoryInterface
from ..utils import ResponseHandler

T = TypeVar('T', bound=Model)

class BaseRepository(BaseRepositoryInterface[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def get_by_id(self, id: int) -> Optional[T]:
        try:
            return await self.model.filter(id=id).first()
        except Exception as e:
            return ResponseHandler.exception(e)

    async def get_all(self) -> List[T]:
        try:
            return await self.model.all()
        except Exception as e:
            return ResponseHandler.exception(e)

    async def create(self, entity: T) -> T:
        try:
            await entity.save()
            return entity
        except Exception as e:
            return ResponseHandler.exception(e)

    async def update(self, id: int, **kwargs) -> Optional[T]:
        try:
            await self.model.filter(id=id).update(**kwargs)
            return await self.get_by_id(id)
        except Exception as e:
            return ResponseHandler.exception(e)

    async def delete(self, id: int) -> bool:
        try:
            deleted_count = await self.model.filter(id=id).delete()
            return deleted_count > 0
        except Exception as e:
            return ResponseHandler.exception(e)