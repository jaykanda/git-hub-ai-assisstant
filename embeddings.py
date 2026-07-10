# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from chunk_splitter import chunk_creation
from vector_metadata import VectorMeta

embedding_model = HuggingFaceEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
)
def vector_creation():
    # for chunk in chunk_creation():
    #     vector = embedding_model.embed_query(
    #         chunk.chunk_text
    #     )
    # also langchain_openai wont support sentence-transformers model
    # so changing to hugging face
    chunks = chunk_creation() # need to conver the chunk list to str, so 
    texts = [chunk.chunk_text for chunk in chunks] # looping the chunks list and get the chunk text alone to text based list
    vectors = embedding_model.embed_documents(texts)
    # print(f"VECTORS OF THE GIVEN CHUNKS ===> {vectors}")
    for chunk, vector in zip(chunks, vectors):
        # print(chunk.path)
        # print(chunk.chunk_id)
        # print(len(vector))
        vector_mdata = VectorMeta(path=chunk.path, id=chunk.id, size=len(vector), vector_data=vector)
        # print(f"VECTORS METADATA ===> {vector_mdata}")
    return vector_mdata

