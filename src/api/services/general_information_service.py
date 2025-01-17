from .base_service import BaseService
from ..models import GeneralInformation
from ..services.interfaces import GeneralInformationServiceInterface

class GeneralInformationService(BaseService[GeneralInformation], GeneralInformationServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)