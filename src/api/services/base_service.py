from typing import Generic, TypeVar
from pydantic import BaseModel as PydanticBaseModel
from ..repositories.interfaces.base_repository_interface import BaseRepositoryInterface
from ..utils import ResponseHandler

T = TypeVar('T')
M = TypeVar('M')

class BaseService(Generic[T, M]):
    def __init__(self, repository: BaseRepositoryInterface[T]):
        self.repository = repository

    async def get_by_id(self, id: int):
        try:
            entity = await self.repository.get_by_id(id)
            if entity:
                return ResponseHandler.success(data=entity)
            return ResponseHandler.error(message="Entity not found", status_code=404)
        except Exception as e:
            return ResponseHandler.exception(e)

    async def get_all(self):
        try:
            entities = await self.repository.get_all()
            return ResponseHandler.success(data=entities)
        except Exception as e:
            return ResponseHandler.exception(e)

    async def create(self, data: PydanticBaseModel):
        try:
            entity_data = data.dict()
            entity = self.repository.model(**entity_data)
            created_entity = await self.repository.create(entity)
            return ResponseHandler.success(data=created_entity, status_code=201)
        except Exception as e:
            return ResponseHandler.exception(e)

    async def update(self, id: int, **kwargs):
        try:
            updated_entity = await self.repository.update(id, **kwargs)
            if updated_entity:
                return ResponseHandler.success(data=updated_entity)
            return ResponseHandler.error(message="Entity not found", status_code=404)
        except Exception as e:
            return ResponseHandler.exception(e)

    async def delete(self, id: int):
        try:
            success = await self.repository.delete(id)
            if success:
                return ResponseHandler.success(message="Entity deleted successfully")
            return ResponseHandler.error(message="Entity not found", status_code=404)
        except Exception as e:
            return ResponseHandler.exception(e)