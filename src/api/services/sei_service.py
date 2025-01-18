from .base_service import BaseService
from ..models import Sei
from ..repositories import SeiRepository
from ..schemas import SeiRequestSchema
from ..services.interfaces import SeiServiceInterface

class SeiService(BaseService[Sei, SeiRequestSchema], SeiServiceInterface):
    def __init__(self, repository = SeiRepository()):
        super().__init__(repository)