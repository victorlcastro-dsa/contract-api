from .base_service import BaseService
from ..models import Attachment
from ..repositories import AttachmentRepository
from ..services.interfaces import AttachmentServiceInterface

class AttachmentService(BaseService[Attachment], AttachmentServiceInterface):
    def __init__(self, repository = AttachmentRepository()):
        super().__init__(repository)