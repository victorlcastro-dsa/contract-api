from .base_service_interface import BaseServiceInterface
from ...models import Union
from ...repositories.interfaces import UnionRepositoryInterface

class UnionServiceInterface(BaseServiceInterface[Union]):
    def __init__(self, repository: UnionRepositoryInterface):
        super().__init__(repository)