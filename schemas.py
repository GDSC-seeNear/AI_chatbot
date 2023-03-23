from typing import Union

from pydantic import BaseModel
from sqlalchemy import DateTime

from models import chat


class request_chat(BaseModel):
    content: str
    is_user_send: bool
    elderly_id: int



class chat(request_chat):
    id: int

    # created_at : DateTime

    class Config:
        orm_mode = True
