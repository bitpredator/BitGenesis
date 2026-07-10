from bitgenesis.memory.object import MemoryObject

from .backend import MemoryBackend


class InMemoryBackend(MemoryBackend):
    """
    Default volatile backend.

    Stores memories only in RAM.
    """

    def __init__(self) -> None:

        self._store: dict[str, MemoryObject] = {}

    def save(
        self,
        memory: MemoryObject,
    ) -> None:

        self._store[memory.id] = memory

    def get(
        self,
        memory_id: str,
    ) -> MemoryObject | None:

        return self._store.get(memory_id)

    def remove(
        self,
        memory_id: str,
    ) -> None:

        self._store.pop(memory_id, None)

    def exists(
        self,
        memory_id: str,
    ) -> bool:

        return memory_id in self._store

    def load(self) -> list[MemoryObject]:

        return list(self._store.values())

    def clear(self) -> None:

        self._store.clear()