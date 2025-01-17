from .base_repository import BaseRepository
from .interfaces import RoleRepositoryInterface
from ..models import Role

class RoleRepository(BaseRepository[Role], RoleRepositoryInterface):
    def __init__(self):
        super().__init__(Role)