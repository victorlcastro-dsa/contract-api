from .base_service import BaseService
from ..models import Sei
from ..repositories import SeiRepository
from ..schemas import SeiRequestSchema
from ..services.interfaces import SeiServiceInterface
from ..utils import check_password

class SeiService(BaseService[Sei, SeiRequestSchema], SeiServiceInterface):
    def __init__(self, repository = SeiRepository()):
        super().__init__(repository)

    def check_password(self, password_hash: str, password: str) -> bool:
        return check_password(password_hash, password) # TODO: Move this responsibility to an authentication location