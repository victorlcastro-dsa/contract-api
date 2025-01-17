from .base_service_interface import BaseServiceInterface
from ...models import Additional
from ...repositories.interfaces import AdditionalRepositoryInterface

class AdditionalServiceInterface(BaseServiceInterface[Additional]):
    def __init__(self, repository: AdditionalRepositoryInterface):
        super().__init__(repository)