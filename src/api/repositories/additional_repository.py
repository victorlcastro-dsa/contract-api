from .base_repository import BaseRepository
from .interfaces import AdditionalRepositoryInterface
from ..models import Additional

class AdditionalRepository(BaseRepository[Additional], AdditionalRepositoryInterface):
    def __init__(self):
        super().__init__(Additional)