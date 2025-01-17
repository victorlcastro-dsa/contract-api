from .base_service_interface import BaseServiceInterface
from ...models import Attachment
from ...repositories.interfaces import AttachmentRepositoryInterface

class AttachmentServiceInterface(BaseServiceInterface[Attachment]):
    def __init__(self, repository: AttachmentRepositoryInterface):
        super().__init__(repository)