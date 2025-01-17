from .base_repository import BaseRepository
from .interfaces import AddressRepositoryInterface
from ..models import Address

class AddressRepository(BaseRepository[Address], AddressRepositoryInterface):
    def __init__(self):
        super().__init__(Address)