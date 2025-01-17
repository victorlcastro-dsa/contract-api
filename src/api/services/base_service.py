from typing import Generic, TypeVar, List, Optional
from ..repositories.interfaces.base_repository_interface import BaseRepositoryInterface

T = TypeVar('T')

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepositoryInterface[T]):
        self.repository = repository

    async def get_by_id(self, id: int) -> Optional[T]:
        return await self.repository.get_by_id(id)

    async def get_all(self) -> List[T]:
        return await self.repository.get_all()

    async def create(self, entity: T) -> T:
        return await self.repository.create(entity)

    async def update(self, id: int, **kwargs) -> Optional[T]:
        return await self.repository.update(id, **kwargs)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)