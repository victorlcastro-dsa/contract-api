from .base_service_interface import BaseServiceInterface
from ...models import Reassignment
from ...repositories.interfaces import ReassignmentRepositoryInterface

class ReassignmentServiceInterface(BaseServiceInterface[Reassignment]):
    def __init__(self, repository: ReassignmentRepositoryInterface):
        super().__init__(repository)