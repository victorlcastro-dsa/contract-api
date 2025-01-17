from pydantic import BaseModel as PydanticBaseModel
from datetime import datetime
from typing import Optional

class BaseRequestSchema(PydanticBaseModel):
    pass

class BaseResponseSchema(PydanticBaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True