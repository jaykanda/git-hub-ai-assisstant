from langchain_text_splitters import RecursiveCharacterTextSplitter
from file_loader import repository_load
from chunk_model import Chunk

def chunk_creation(): 
    all_chunks = [] 
    chunk_len = 0 
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    # print(f"Invoking the documents from repository_load function {repository_load()}")
    for document in repository_load():
        chunks = splitter.split_text(document.content)
        for index, chunk in enumerate(chunks, start=1):
            # print(document.path)
            # print(f"------------ Chunk Id - {index}------------", "\n")
            # print(chunk)
            chunk_data = Chunk(path=document.path, chunk_id=index, chunk_text=chunk, chunk_size=len(chunk))
            all_chunks.append(chunk_data)
            chunk_len += len(all_chunks)
    # print(f"ALL CHUNK LENGTH ====> {chunk_len}")
    return all_chunks
                            