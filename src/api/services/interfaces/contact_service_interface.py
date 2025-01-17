from .base_service_interface import BaseServiceInterface
from ...models import Contact
from ...repositories.interfaces import ContactRepositoryInterface

class ContactServiceInterface(BaseServiceInterface[Contact]):
    def __init__(self, repository: ContactRepositoryInterface):
        super().__init__(repository)