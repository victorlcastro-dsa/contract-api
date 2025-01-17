from .base_service import BaseService
from ..models import Union
from ..services.interfaces import UnionServiceInterface

class UnionService(BaseService[Union], UnionServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)