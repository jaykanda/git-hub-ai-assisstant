from pydantic import BaseModel

class ChatRequest(BaseModel):
    userquery: str