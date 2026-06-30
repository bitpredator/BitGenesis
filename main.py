from bitgenesis.kernel.bootstrap import bootstrap
from bitgenesis.events.types import Event


bus, kernel, memory_store = bootstrap()

bus.emit(Event(
    type="perception.event",
    source="system",
    payload={
        "input": "hello world",
        "context": "test memory system"
    }
))

print("Memories stored:", len(memory_store.get_all()))