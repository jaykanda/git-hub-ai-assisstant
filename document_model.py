from dataclasses import dataclass

@dataclass
class Document:
    path: str
    extension: str
    content: str
    size: int