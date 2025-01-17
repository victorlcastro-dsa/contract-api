from .base_service import BaseService
from ..models import OrganizationClient
from ..services.interfaces import OrganizationClientServiceInterface

class OrganizationClientService(BaseService[OrganizationClient], OrganizationClientServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)