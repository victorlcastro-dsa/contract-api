from .base_service import BaseService
from ..models import Item
from ..services.interfaces import ItemServiceInterface

class ItemService(BaseService[Item], ItemServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)