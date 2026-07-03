from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)

from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.memory.store import MemoryStore

from bitgenesis.reasoning.session import ReasoningSession


def test_reasoning_session_returns_decision():

    store = MemoryStore()

    # Inserisce una memoria nello store
    memory = MemoryFactory.from_event(
        Event(
            category=EventCategory.SYSTEM,
            type=EventType.SYSTEM_STARTED,
            source="bootstrap",
            payload={"message": "BitGenesis started"},
            priority=EventPriority.NORMAL,
        )
    )

    store.add(memory)

    session = ReasoningSession(store)

    # Evento da elaborare
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        payload={"message": "Hello"},
        priority=EventPriority.NORMAL,
    )

    decision = session.process(event)

    assert decision is not None
    assert hasattr(decision, "action")
    assert hasattr(decision, "confidence")
    assert hasattr(decision, "explanation")