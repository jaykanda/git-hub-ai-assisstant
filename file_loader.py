from utils import SUPPORTED_EXTENSIONS, IGNORE_DIRS
import os
from config import REPO_URL
from document_model import Document

def repository_load():
    documents = []
    for root, dirs, files in os.walk("./repository/digital-twin-python-agent"): 
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            print(f"CURRENT FILE ==> {file}")
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]

            if ext not in SUPPORTED_EXTENSIONS: 
                continue

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                file_content = f.read() 
                file_doc = Document(path = file_path, extension = ext, content = file_content, size = len(file_content))
                documents.append(file_doc) 
                print(f"DOCUMENT FETCHED ===> {documents}")
    return documents 