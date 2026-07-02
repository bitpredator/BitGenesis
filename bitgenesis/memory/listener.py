from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.memory.processor import MemoryProcessor


class MemoryListener:
    """
    Listens to events and converts them into MemoryObjects.
    """

    def __init__(self, store):
        self._store = store
        self._processor = MemoryProcessor()

    def handle(self, event) -> None:
        """
        Convert event → memory → process → store
        """

        memory = MemoryFactory.from_event(event)
        memory = self._processor.process(memory)

        # IMPORTANT: use add() (test expects store.add)
        self._store.add(memory)