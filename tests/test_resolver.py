from bitgenesis.reasoning.intent_detector import IntentDetector
from bitgenesis.reasoning.resolver import Resolver
from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.factory import MemoryFactory

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)


def test_resolver_returns_creator():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("Who created you?")

    resolution = resolver.resolve(intent)

    assert resolution.domain == "identity"
    assert resolution.target == "creator"
    assert resolution.value == "Bitpredator"
    assert resolution.success is True


def test_resolver_returns_name():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your name?")

    resolution = resolver.resolve(intent)

    assert resolution.value == "BitGenesis"


def test_resolver_returns_project():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your project?")

    resolution = resolver.resolve(intent)

    assert resolution.value == "BitGenesis"


def test_resolver_returns_version():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your version?")

    resolution = resolver.resolve(intent)

    assert resolution.value == "0.2.0"


def test_resolver_returns_none_for_unknown_domain():

    class FakeIntent:
        domain = "unknown"
        target = "anything"

    resolver = Resolver()

    resolution = resolver.resolve(FakeIntent())

    assert resolution is None


def test_resolver_returns_none_for_none_intent():

    resolver = Resolver()

    assert resolver.resolve(None) is None

def create_memory(message):

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        payload={"message": message},
        priority=EventPriority.NORMAL,
    )

    return MemoryFactory.from_event(event)


def test_resolver_returns_latest_memory():

    store = MemoryStore()

    store.add(create_memory("First"))
    store.add(create_memory("Second"))

    detector = IntentDetector()
    resolver = Resolver(memory_store=store)

    intent = detector.detect(
        "What is your latest memory?"
    )

    resolution = resolver.resolve(intent)

    assert resolution.domain == "memory"
    assert resolution.target == "latest"

    assert (
        resolution.value.content["payload"]["message"]
        == "Second"
    )


def test_resolver_returns_recent_memories():

    store = MemoryStore()

    for i in range(5):
        store.add(create_memory(f"Memory {i}"))

    detector = IntentDetector()
    resolver = Resolver(memory_store=store)

    intent = detector.detect(
        "What do you remember?"
    )

    resolution = resolver.resolve(intent)

    assert resolution.domain == "memory"
    assert resolution.target == "recent"

    assert len(resolution.value) == 5

def test_resolver_returns_memory_search():

    store = MemoryStore()

    store.add(create_memory("Planner initialized"))
    store.add(create_memory("Memory subsystem ready"))

    detector = IntentDetector()
    resolver = Resolver(memory_store=store)

    intent = detector.detect(
        "What do you remember about planner?"
    )

    resolution = resolver.resolve(intent)

    assert resolution.domain == "memory"
    assert resolution.target == "planner"
    assert len(resolution.value) == 1
    assert resolution.value[0].content["payload"]["message"] == "Planner initialized"

def test_resolver_uses_memory_retrieval():

    store = MemoryStore()

    store.add(create_memory("Python module created"))
    store.add(create_memory("Planner initialized"))

    detector = IntentDetector()
    resolver = Resolver(memory_store=store)

    intent = detector.detect(
        "What do you remember about Python?"
    )

    resolution = resolver.resolve(intent)

    assert resolution.domain == "memory"
    assert resolution.target == "python"

    assert len(resolution.value) == 1

    assert (
        resolution.value[0]
        .content["payload"]["message"]
        ==
        "Python module created"
    )