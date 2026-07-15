from dataclasses import dataclass

@dataclass
class VectorMeta:
    path: str
    id: int
    size: int
    vector_data: list