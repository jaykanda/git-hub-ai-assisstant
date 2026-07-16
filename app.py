# import clone_repo
import file_loader
from chunk_splitter import chunk_creation
from vectordb import vector_Store
from retriever import retrieval_search
from fastapi import FastAPI

app = FastAPI()

chunk_creation()
vector_Store()
user_query = input("Ask : ")
results = retrieval_search(user_query)

for result in results:
    print(result.page_content, "\n")
    print("======================")    