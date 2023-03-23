from fastapi import FastAPI
from pydantic import BaseModel

from chatbot_class import chat

app = FastAPI()

class chat_text(BaseModel):
    text : str


@app.post("/")
def read_root(request: chat_text):
    a = chat()
    output = a(request.text)

    return output

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}