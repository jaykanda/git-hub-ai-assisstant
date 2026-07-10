# import clone_repo
import file_loader
from chunk_splitter import chunk_creation
from embeddings import vector_creation
from vectordb import vector_Store
from dotenv import load_dotenv

load_dotenv()
chunk_creation()
vector_creation()
vector_Store()