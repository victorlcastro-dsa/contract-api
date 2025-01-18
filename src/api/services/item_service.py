from .base_service import BaseService
from ..models import Item
from ..repositories import ItemRepository
from ..schemas import ItemRequestSchema
from ..services.interfaces import ItemServiceInterface

class ItemService(BaseService[Item, ItemRequestSchema], ItemServiceInterface):
    def __init__(self, repository = ItemRepository()):
        super().__init__(repository)