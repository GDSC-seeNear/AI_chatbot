from pydantic.schema import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from database import Base


class chat(Base):
    __tablename__ = "chat"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String)
    userSend = Column(Boolean, name='user_send')
    elderlyId = Column(Integer, name='elderly_id')
    type = Column(String, nullable=True)
    createdAt = Column(DateTime, default=func.now(), name='created_at')
