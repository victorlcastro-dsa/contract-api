from .base_service import BaseService
from ..models import GeneralInformation
from ..repositories import GeneralInformationRepository
from ..schemas import GeneralInformationRequestSchema
from ..services.interfaces import GeneralInformationServiceInterface

class GeneralInformationService(BaseService[GeneralInformation, GeneralInformationRequestSchema], GeneralInformationServiceInterface):
    def __init__(self, repository = GeneralInformationRepository()):
        super().__init__(repository)