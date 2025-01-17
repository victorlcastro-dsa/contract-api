from .base_repository import BaseRepository
from .interfaces import OrganizationClientRepositoryInterface
from ..models import OrganizationClient

class OrganizationClientRepository(BaseRepository[OrganizationClient], OrganizationClientRepositoryInterface):
    def __init__(self):
        super().__init__(OrganizationClient)