from .base_service import BaseService
from ..models import Address
from ..repositories import AddressRepository
from ..services.interfaces import AddressServiceInterface

class AddressService(BaseService[Address], AddressServiceInterface):
    def __init__(self, repository = AddressRepository()):
        super().__init__(repository)