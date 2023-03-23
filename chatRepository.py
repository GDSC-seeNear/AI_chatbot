from sqlalchemy.orm import Session

from . import models, schemas

def create_chat(db: Session, chat: schemas.request_chat):
    db_chat = models.chat(content=chat.content, is_user_send=chat.is_user_send, elderly_id=chat.elderly_id)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat