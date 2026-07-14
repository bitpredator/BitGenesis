from bitgenesis.dialogue.response_engine import ResponseEngine
from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.factory import MemoryFactory

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)


def test_response_engine_returns_creator():

    engine = ResponseEngine()

    response = engine.respond("Who created you?")

    assert response == "My creator is Bitpredator."


def test_response_engine_returns_name():

    engine = ResponseEngine()

    response = engine.respond("What is your name?")

    assert response == "I am BitGenesis."


def test_response_engine_returns_project():

    engine = ResponseEngine()

    response = engine.respond("What is your project?")

    assert response == "My project is BitGenesis."


def test_response_engine_returns_version():

    engine = ResponseEngine()

    response = engine.respond("What is your version?")

    assert response == "I am currently running version 0.2.0."


def test_response_engine_returns_description():

    engine = ResponseEngine()

    response = engine.respond("Describe yourself")

    assert response is not None
    assert "modular cognitive ai framework" in response.lower()


def test_response_engine_returns_none_for_unknown_question():

    engine = ResponseEngine()

    response = engine.respond("How is the weather today?")

    assert response is None


def test_response_engine_returns_none_for_empty_question():

    engine = ResponseEngine()

    response = engine.respond("")

    assert response is None


def create_memory(message):

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        payload={"message": message},
        priority=EventPriority.NORMAL,
    )

    return MemoryFactory.from_event(event)


def test_response_engine_returns_latest_memory():

    store = MemoryStore()

    store.add(create_memory("System boot"))
    store.add(create_memory("Planner initialized"))

    engine = ResponseEngine(memory_store=store)

    response = engine.respond(
        "What is your latest memory?"
    )

    assert response is not None
    assert "Planner initialized" in response


def test_response_engine_returns_recent_memories():

    store = MemoryStore()

    store.add(create_memory("Memory A"))
    store.add(create_memory("Memory B"))
    store.add(create_memory("Memory C"))

    engine = ResponseEngine(memory_store=store)

    response = engine.respond(
        "What do you remember?"
    )

    assert response is not None

    assert "Memory A" in response
    assert "Memory B" in response
    assert "Memory C" in response