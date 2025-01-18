from .base_service import BaseService
from ..models import Item
from ..repositories import ItemRepository
from ..services.interfaces import ItemServiceInterface

class ItemService(BaseService[Item], ItemServiceInterface):
    def __init__(self, repository = ItemRepository()):
        super().__init__(repository)