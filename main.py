from bitgenesis.kernel.bootstrap import bootstrap
from bitgenesis.events.types import Event


bus, kernel = bootstrap()

event = Event(
    type="perception.event",
    source="system",
    payload={
        "type": "system.boot",
        "data": "BitGenesis online"
    }
)

bus.emit(event)