from pydantic.schema import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class chat(Base):
    __tablename__ = "chat"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    content = Column(String,unique=True)
    is_user_send = Column(Boolean)
    elderly_id = Column(Integer)
    # created_at = Column(DateTime)