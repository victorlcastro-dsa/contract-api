from .base_service import BaseService
from ..models import Reassignment
from ..services.interfaces import ReassignmentServiceInterface

class ReassignmentService(BaseService[Reassignment], ReassignmentServiceInterface):
    def __init__(self, repository):
        super().__init__(repository)