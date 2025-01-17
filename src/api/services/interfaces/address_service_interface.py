from .base_service_interface import BaseServiceInterface
from ...models import Address
from ...repositories.interfaces import AddressRepositoryInterface

class AddressServiceInterface(BaseServiceInterface[Address]):
    def __init__(self, repository: AddressRepositoryInterface):
        super().__init__(repository)