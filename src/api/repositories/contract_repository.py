from .base_repository import BaseRepository
from .interfaces import ContractRepositoryInterface
from ..models import Contract

class ContractRepository(BaseRepository[Contract], ContractRepositoryInterface):
    def __init__(self):
        super().__init__(Contract)