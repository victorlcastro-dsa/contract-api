from .base_service_interface import BaseServiceInterface
from ...models import GeneralInformation
from ...repositories.interfaces import GeneralInformationRepositoryInterface

class GeneralInformationServiceInterface(BaseServiceInterface[GeneralInformation]):
    def __init__(self, repository: GeneralInformationRepositoryInterface):
        super().__init__(repository)