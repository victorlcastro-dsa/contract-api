from .base_repository import BaseRepository
from .interfaces import ContactRepositoryInterface
from ..models import Contact

class ContactRepository(BaseRepository[Contact], ContactRepositoryInterface):
    def __init__(self):
        super().__init__(Contact)