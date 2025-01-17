from .base_service_interface import BaseServiceInterface
from ...models import Role
from ...repositories.interfaces import RoleRepositoryInterface

class RoleServiceInterface(BaseServiceInterface[Role]):
    def __init__(self, repository: RoleRepositoryInterface):
        super().__init__(repository)