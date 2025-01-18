from .base_service import BaseService
from ..models import Role
from ..repositories import RoleRepository
from ..services.interfaces import RoleServiceInterface

class RoleService(BaseService[Role], RoleServiceInterface):
    def __init__(self, repository = RoleRepository()):
        super().__init__(repository)