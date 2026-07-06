from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)
from bitgenesis.dialogue.response_engine import ResponseEngine


def create_memory(message: str):
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="demo",
        payload={"message": message},
        priority=EventPriority.NORMAL,
    )
    return MemoryFactory.from_event(event)


store = MemoryStore()

store.add(create_memory("BitGenesis started"))
store.add(create_memory("Planner initialized"))
store.add(create_memory("Memory subsystem ready"))

engine = ResponseEngine(memory_store=store)

print(engine.respond("Who created you?"))
print(engine.respond("What is your name?"))
print(engine.respond("What is your latest memory?"))
print(engine.respond("What do you remember?"))