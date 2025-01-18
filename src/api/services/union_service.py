from .base_service import BaseService
from ..models import Union
from ..repositories import UnionRepository
from ..schemas import UnionRequestSchema
from ..services.interfaces import UnionServiceInterface

class UnionService(BaseService[Union, UnionRequestSchema], UnionServiceInterface):
    def __init__(self, repository = UnionRepository()):
        super().__init__(repository)