from .base_repository import BaseRepository
from .interfaces import ReassignmentRepositoryInterface
from ..models import Reassignment

class ReassignmentRepository(BaseRepository[Reassignment], ReassignmentRepositoryInterface):
    def __init__(self):
        super().__init__(Reassignment)