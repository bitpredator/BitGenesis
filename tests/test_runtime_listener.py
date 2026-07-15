from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)
from bitgenesis.events.event_bus import EventBus

from bitgenesis.memory.listeners.runtime_listener import (
    RuntimeEpisodeListener,
)
from bitgenesis.memory.store import MemoryStore


def make_runtime_event():

    return Event(
        category=EventCategory.RUNTIME,
        type=EventType.ACTION_COMPLETED,
        source="executor",
        payload={
            "action": "test",
        },
        priority=EventPriority.NORMAL,
    )


def test_listener_accepts_runtime_event():

    store = MemoryStore()

    listener = RuntimeEpisodeListener(store)

    listener.handle(
        make_runtime_event()
    )

    assert len(store.all()) == 1


def test_listener_ignores_other_categories():

    store = MemoryStore()

    listener = RuntimeEpisodeListener(store)

    listener.handle(
        Event(
            category=EventCategory.SYSTEM,
            type=EventType.SYSTEM_STARTED,
            source="kernel",
            priority=EventPriority.NORMAL,
        )
    )

    assert len(store.all()) == 0


def test_listener_can_be_registered_on_event_bus():

    store = MemoryStore()

    bus = EventBus()

    listener = RuntimeEpisodeListener(store)

    bus.subscribe(
        EventCategory.RUNTIME,
        listener,
    )

    bus.publish(
        make_runtime_event()
    )

    assert len(store.all()) == 1