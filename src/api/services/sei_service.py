from .base_service import BaseService
from ..models import Sei
from ..repositories import SeiRepository
from ..services.interfaces import SeiServiceInterface

class SeiService(BaseService[Sei], SeiServiceInterface):
    def __init__(self, repository = SeiRepository()):
        super().__init__(repository)