from pydantic import BaseModel as PydanticBaseModel
from datetime import datetime
from typing import Optional, List, TypeVar, Generic

T = TypeVar('T')

class BaseRequestSchema(PydanticBaseModel):
    pass

class BaseResponseSchema(PydanticBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class BaseListResponseSchema(PydanticBaseModel, Generic[T]):
    items: List[T]