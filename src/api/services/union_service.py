from .base_service import BaseService
from ..models import Union
from ..repositories import UnionRepository
from ..services.interfaces import UnionServiceInterface

class UnionService(BaseService[Union], UnionServiceInterface):
    def __init__(self, repository = UnionRepository()):
        super().__init__(repository)