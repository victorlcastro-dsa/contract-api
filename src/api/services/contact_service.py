from .base_service import BaseService
from ..models import Contact
from ..repositories import ContactRepository
from ..schemas import ContactRequestSchema
from ..services.interfaces import ContactServiceInterface

class ContactService(BaseService[Contact, ContactRequestSchema], ContactServiceInterface):
    def __init__(self, repository = ContactRepository()):
        super().__init__(repository)