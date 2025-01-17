from .base_service_interface import BaseServiceInterface
from ...models import Contract
from ...repositories.interfaces import ContractRepositoryInterface

class ContractServiceInterface(BaseServiceInterface[Contract]):
    def __init__(self, repository: ContractRepositoryInterface):
        super().__init__(repository)