import datetime
from json import JSONEncoder

from chatbot_class import chat

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from schemas import request_chat
import chatRepository, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app = FastAPI()
app.json_encoder = CustomJSONEncoder


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/")
def read_root(request: request_chat,db: Session = Depends(get_db)):

    after_chat = chatRepository.create_chat(db,request)

    a = chat()
    output = a(request.content)

    new_chat = {"content":output,"is_user_send":False,"elderly_id":request.elderly_id}
    response_chat = request_chat(**new_chat)
    before_chat = chatRepository.create_chat(db,response_chat)


    return output

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}