from .base_service import BaseService
from ..models import Role
from ..services.interfaces import RoleServiceInterface

class RoleService(BaseService[Role], RoleServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)