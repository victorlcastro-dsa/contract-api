from .base_service import BaseService
from ..models import Attachment
from ..repositories import AttachmentRepository
from ..schemas import AttachmentRequestSchema
from ..services.interfaces import AttachmentServiceInterface

class AttachmentService(BaseService[Attachment, AttachmentRequestSchema], AttachmentServiceInterface):
    def __init__(self, repository = AttachmentRepository()):
        super().__init__(repository)