from langchain_chroma import Chroma
from embeddings import embedding_model
from chunk_splitter import chunk_creation

def vector_Store():
    vector_store = Chroma(
        collection_name = "github_repo",
        embedding_function = embedding_model,
        persist_directory = "./vector_db"
    )
    vector_store.add_documents(chunk_creation())