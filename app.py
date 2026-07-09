import clone_repo
import file_loader
from file_loader import repository_load

doc_content = repository_load()
print(f"DOCUMENT LIST FROM APP ===> {doc_content}")