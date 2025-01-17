from .base_service_interface import BaseServiceInterface
from ...models import Sei
from ...repositories.interfaces import SeiRepositoryInterface

class SeiServiceInterface(BaseServiceInterface[Sei]):
    def __init__(self, repository: SeiRepositoryInterface):
        super().__init__(repository)