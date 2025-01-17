from .base_repository import BaseRepository
from .interfaces import ItemRepositoryInterface
from ..models import Item

class ItemRepository(BaseRepository[Item], ItemRepositoryInterface):
    def __init__(self):
        super().__init__(Item)