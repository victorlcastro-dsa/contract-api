from .base_repository import BaseRepository
from .interfaces import UnionRepositoryInterface
from ..models import Union

class UnionRepository(BaseRepository[Union], UnionRepositoryInterface):
    def __init__(self):
        super().__init__(Union)