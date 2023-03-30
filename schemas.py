from typing import Optional, Union

from pydantic import BaseModel
from sqlalchemy import DateTime

from models import chat


class request_chat(BaseModel):
    content: str
    userSend: bool
    elderlyId: int
    type: Optional[str] = None


class chat(request_chat):
    id: int

    class Config:
        orm_mode = True
