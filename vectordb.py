from langchain_chroma import Chroma
from langchain_core.documents import Document as LCDocument
from embeddings import embedding_model
from chunk_splitter import chunk_creation

def vector_Store():
    vector_store = Chroma(
        collection_name = "github_repo",
        embedding_function = embedding_model,
        persist_directory = "./vector_db"
    )
    chunks = chunk_creation()
    lcdocuments = []

    for chunk in chunks:
        LCdoc = LCDocument(
            page_content= chunk.chunk_text,
            metadata = {
                "path" : chunk.path,
                "chunk_id" : chunk.chunk_id,
                "chunk_size" : chunk.chunk_size
            }
        )
        lcdocuments.append(LCdoc)

    vector_store.add_documents(lcdocuments)
    return vector_store 