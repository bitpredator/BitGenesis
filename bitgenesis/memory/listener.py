from bitgenesis.events.types import Event
from bitgenesis.memory.types import Memory
from bitgenesis.memory.store import MemoryStore


class MemoryListener:
    def __init__(self, store: MemoryStore):
        self.store = store

    def handle(self, event: Event):
        memory = Memory(
            type=event.type,
            content=event.payload,
            event_id=event.id
        )

        self.store.save(memory)