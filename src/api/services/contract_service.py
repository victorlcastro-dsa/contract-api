from .base_service import BaseService
from ..models import Contract
from ..repositories import ContractRepository
from ..schemas import ContractRequestSchema
from ..services.interfaces import ContractServiceInterface

class ContractService(BaseService[Contract, ContractRequestSchema], ContractServiceInterface):
    def __init__(self, repository = ContractRepository()):
        super().__init__(repository)