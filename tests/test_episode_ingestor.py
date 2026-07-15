from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)
from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.memory.episode.ingestor import EpisodeIngestor


class DummyEpisodeManager:
    def __init__(self):
        self.memories = []

    def append(self, memory):
        self.memories.append(memory)


def make_memory():

    event = Event(
        category=EventCategory.RUNTIME,
        type=EventType.ACTION_COMPLETED,
        source="executor",
        payload={
            "action": "test",
        },
        priority=EventPriority.NORMAL,
    )

    return MemoryFactory.from_event(event)


def test_ingestor_appends_memory():

    manager = DummyEpisodeManager()

    ingestor = EpisodeIngestor(
        manager
    )

    memory = make_memory()

    ingestor.ingest(memory)

    assert len(manager.memories) == 1


def test_ingestor_ignores_none():

    manager = DummyEpisodeManager()

    ingestor = EpisodeIngestor(
        manager
    )

    ingestor.ingest(None)

    assert len(manager.memories) == 0


def test_ingestor_passes_same_memory_instance():

    manager = DummyEpisodeManager()

    ingestor = EpisodeIngestor(
        manager
    )

    memory = make_memory()

    ingestor.ingest(memory)

    assert manager.memories[0] is memory