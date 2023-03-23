from fastapi import FastAPI
from pydantic import BaseModel

from chatbot_class import chat

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class request_chat(BaseModel):
    content : str,
    is_user_send bool,
    elderly_id int


@app.post("/")
def read_root(request: request_chat,db: Session = Depends(get_db)):

    a = chat()
    output = a(request.content)

    return output

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}