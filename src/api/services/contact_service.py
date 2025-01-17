from .base_service import BaseService
from ..models import Contact
from ..services.interfaces import ContactServiceInterface

class ContactService(BaseService[Contact], ContactServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)