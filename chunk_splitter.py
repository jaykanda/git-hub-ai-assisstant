from langchain_text_splitters import RecursiveCharacterTextSplitter
from file_loader import repository_load
from chunk_model import Chunk

def chunk_creation(): 
    all_chunks = []  
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    # print(f"Invoking the documents from repository_load function {repository_load()}")
    for document in repository_load():
        chunks = splitter.split_text(document.content)
        for index, chunk in enumerate(chunks, start=1):
            # print(document.path, "\n")
            # print(f"------------ Chunk Id - {index}------------ Chunk size - {len(chunk)}", "\n")
            # print(chunk, "\n")
            chunk_data = Chunk(path=document.path, id=index, chunk_text=chunk, size=len(chunk))
            all_chunks.append(chunk_data)
    return all_chunks
                            