from .base_service import BaseService
from ..models import OrganizationClient
from ..repositories import OrganizationClientRepository
from ..schemas import OrganizationClientRequestSchema
from ..services.interfaces import OrganizationClientServiceInterface

class OrganizationClientService(BaseService[OrganizationClient, OrganizationClientRequestSchema], OrganizationClientServiceInterface):
    def __init__(self, repository = OrganizationClientRepository()):
        super().__init__(repository)