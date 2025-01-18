from .base_service import BaseService
from ..models import Additional
from ..repositories import AdditionalRepository
from ..schemas import AdditionalRequestSchema
from ..services.interfaces import AdditionalServiceInterface

class AdditionalService(BaseService[Additional, AdditionalRequestSchema], AdditionalServiceInterface):
    def __init__(self, repository = AdditionalRepository()):
        super().__init__(repository)