from .base_service import BaseService
from ..models import Sei
from ..services.interfaces import SeiServiceInterface

class SeiService(BaseService[Sei], SeiServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)