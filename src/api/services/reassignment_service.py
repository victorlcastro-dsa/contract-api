from .base_service import BaseService
from ..models import Reassignment
from ..repositories import ReassignmentRepository
from ..services.interfaces import ReassignmentServiceInterface

class ReassignmentService(BaseService[Reassignment], ReassignmentServiceInterface):
    def __init__(self, repository = ReassignmentRepository()):
        super().__init__(repository)