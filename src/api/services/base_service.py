from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel as PydanticBaseModel
from ..repositories.interfaces.base_repository_interface import BaseRepositoryInterface

T = TypeVar('T')
M = TypeVar('M')

class BaseService(Generic[T, M]):
    def __init__(self, repository: BaseRepositoryInterface[T]):
        self.repository = repository

    async def get_by_id(self, id: int) -> Optional[T]:
        return await self.repository.get_by_id(id)

    async def get_all(self) -> List[T]:
        return await self.repository.get_all()

    async def create(self, data: PydanticBaseModel) -> T:
        entity_data = data.dict()
        entity = self.repository.model(**entity_data)
        return await self.repository.create(entity)

    async def update(self, id: int, **kwargs) -> Optional[T]:
        return await self.repository.update(id, **kwargs)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)