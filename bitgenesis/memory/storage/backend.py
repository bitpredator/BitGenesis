from abc import ABC
from abc import abstractmethod

from bitgenesis.memory.object import MemoryObject


class MemoryBackend(ABC):
    """
    Abstract persistence backend for MemoryStore.

    Concrete implementations are responsible for storing
    and restoring MemoryObject instances.
    """

    @abstractmethod
    def save(self, memory: MemoryObject) -> None:
        """
        Persist a memory object.
        """

    @abstractmethod
    def get(self, memory_id: str) -> MemoryObject | None:
        """
        Retrieve a memory by its identifier.
        """

    @abstractmethod
    def remove(self, memory_id: str) -> None:
        """
        Remove a memory.
        """

    @abstractmethod
    def exists(self, memory_id: str) -> bool:
        """
        Returns True if the memory exists.
        """

    @abstractmethod
    def load(self) -> list[MemoryObject]:
        """
        Load all memories.
        """

    @abstractmethod
    def clear(self) -> None:
        """
        Remove every stored memory.
        """