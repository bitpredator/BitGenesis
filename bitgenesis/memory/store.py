
from typing import List, Optional
from bitgenesis.memory.types import Memory


class MemoryStore:
    def __init__(self):
        self.memories: List[Memory] = []

    def save(self, memory: Memory):
        self.memories.append(memory)

    def query_by_type(self, memory_type: str) -> List[Memory]:
        return [m for m in self.memories if m.type == memory_type]

    def get_all(self) -> List[Memory]:
        return self.memories