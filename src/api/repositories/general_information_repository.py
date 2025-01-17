from .base_repository import BaseRepository
from .interfaces import GeneralInformationRepositoryInterface
from ..models import GeneralInformation

class GeneralInformationRepository(BaseRepository[GeneralInformation], GeneralInformationRepositoryInterface):
    def __init__(self):
        super().__init__(GeneralInformation)