from .base_service_interface import BaseServiceInterface
from ...models import OrganizationClient
from ...repositories.interfaces import OrganizationClientRepositoryInterface

class OrganizationClientServiceInterface(BaseServiceInterface[OrganizationClient]):
    def __init__(self, repository: OrganizationClientRepositoryInterface):
        super().__init__(repository)