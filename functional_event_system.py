from __future__ import annotations


from bitgenesis.events.event_bus import (
    EventBus,
)

from bitgenesis.events.event import (
    Event,
)

from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)



print("=== Event System Functional Test ===")



# --------------------------------------------------
# Setup
# --------------------------------------------------

bus = EventBus()


received = {
    "count": 0,
    "event": None,
}



def event_listener(
    event,
):

    received["count"] += 1
    received["event"] = event



# --------------------------------------------------
# Subscribe
# --------------------------------------------------

bus.subscribe(
    EventType.RUNTIME_STARTED,
    event_listener,
)



assert bus.subscriber_count(
    EventType.RUNTIME_STARTED
) == 1



print(
    "Subscriber registered"
)



# --------------------------------------------------
# Emit Event
# --------------------------------------------------

event = Event(
    category=EventCategory.RUNTIME,
    type=EventType.RUNTIME_STARTED,
    source="functional_test",
    payload={
        "status": "running",
        "test": True,
    },
)



bus.emit(
    event
)



print(
    "Event emitted"
)



# --------------------------------------------------
# Validate delivery
# --------------------------------------------------

assert received["count"] == 1


assert received["event"] is not None


assert received["event"].type == EventType.RUNTIME_STARTED


assert received["event"].source == "functional_test"


assert received["event"].payload["status"] == "running"


assert received["event"].payload["test"] is True



print(
    "Event received correctly"
)



# --------------------------------------------------
# Category subscription
# --------------------------------------------------

category_received = {
    "value": False,
}



def category_listener(
    event,
):

    category_received["value"] = True



bus.subscribe(
    EventCategory.RUNTIME,
    category_listener,
)



bus.emit(
    Event(
        category=EventCategory.RUNTIME,
        type=EventType.RUNTIME_STOPPED,
        source="functional_test",
        payload={},
    )
)



assert category_received["value"] is True


print(
    "Category routing OK"
)



# --------------------------------------------------
# Unsubscribe
# --------------------------------------------------

bus.unsubscribe(
    EventType.RUNTIME_STARTED,
    event_listener,
)



assert bus.subscriber_count(
    EventType.RUNTIME_STARTED
) == 0



print(
    "Unsubscribe OK"
)



# --------------------------------------------------
# Clear
# --------------------------------------------------

bus.clear()


assert bus.subscriber_count() == 0



print(
    "Clear OK"
)



print(
    "=== Event System Test OK ==="
)