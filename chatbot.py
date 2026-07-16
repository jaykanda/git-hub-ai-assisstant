from fastapi import APIRouter
from models.chat_request import ChatRequest
from retriever import retrieval_search
from prompt_builder import build_Prompt

router = APIRouter()

@router.post("/chat")
def chatBot(request: ChatRequest):
    print(f"user query in the chat request ==> ", request.userquery)
    documents = retrieval_search(request.userquery)
    build_Prompt(request.userquery, documents)

    

    
