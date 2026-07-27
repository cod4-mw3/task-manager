from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Title cannot be empty")
        if len(v) > 255:
            raise ValueError("Title must be 255 characters or fewer")
        return v

    @field_validator("description")
    @classmethod
    def description_max_length(cls, v):
        if v and len(v) > 1000:
            raise ValueError("Description must be 1000 characters or fewer")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, v):
        if v is not None:
            v = v.strip()
            if not v:
                raise ValueError("Title cannot be empty")
            if len(v) > 255:
                raise ValueError("Title must be 255 characters or fewer")
        return v

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
