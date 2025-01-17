from .base_repository import BaseRepository
from .interfaces import AttachmentRepositoryInterface
from ..models import Attachment

class AttachmentRepository(BaseRepository[Attachment], AttachmentRepositoryInterface):
    def __init__(self):
        super().__init__(Attachment)