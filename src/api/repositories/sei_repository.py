from .base_repository import BaseRepository
from .interfaces import SeiRepositoryInterface
from ..models import Sei

class SeiRepository(BaseRepository[Sei], SeiRepositoryInterface):
    def __init__(self):
        super().__init__(Sei)