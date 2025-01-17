from .base_service import BaseService
from ..models import Contract
from ..services.interfaces import ContractServiceInterface

class ContractService(BaseService[Contract], ContractServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)