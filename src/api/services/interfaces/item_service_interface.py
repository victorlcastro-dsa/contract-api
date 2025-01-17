from .base_service_interface import BaseServiceInterface
from ...models import Item
from ...repositories.interfaces import ItemRepositoryInterface

class ItemServiceInterface(BaseServiceInterface[Item]):
    def __init__(self, repository: ItemRepositoryInterface):
        super().__init__(repository)