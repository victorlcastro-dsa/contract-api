from .base_service import BaseService
from ..models import Additional
from ..services.interfaces import AdditionalServiceInterface

class AdditionalService(BaseService[Additional], AdditionalServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)