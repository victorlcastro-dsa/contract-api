from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class BaseRepositoryInterface(Generic[T]):
    async def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError

    async def get_all(self) -> List[T]:
        raise NotImplementedError

    async def create(self, entity: T) -> T:
        raise NotImplementedError

    async def update(self, id: int, **kwargs) -> Optional[T]:
        raise NotImplementedError

    async def delete(self, id: int) -> bool:
        raise NotImplementedError