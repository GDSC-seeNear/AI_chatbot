from sqlalchemy.orm import Session

import models
import schemas


def create_chat(db: Session, chat: schemas.request_chat):
    print(chat)
    db_chat = models.chat(content=chat.content,
                          userSend=chat.userSend, elderlyId=chat.elderlyId)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat
