from dataclasses import dataclass

@dataclass
class Chunk:
    path: str
    chunk_id: int
    chunk_text: str
    chunk_size: int