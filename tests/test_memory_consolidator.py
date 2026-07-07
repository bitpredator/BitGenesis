from bitgenesis.memory.consolidator import MemoryConsolidator


class FakeMemory:

    def __init__(self, message):

        self.content = {
            "payload": {
                "message": message,
            }
        }


class FakeEpisode:

    def __init__(self, memories):

        self.memories = memories


class FakeExtractor:

    def extract(self, memory):

        message = (
            memory.content
            .get("payload", {})
            .get("message")
        )

        if message == "ignore":
            return None

        return {
            "fact": message,
        }


class FakeRegistry:

    def __init__(self):

        self.items = []

    def add(self, fact):

        self.items.append(fact)


def test_consolidate_empty_episode():

    consolidator = MemoryConsolidator(
        extractor=FakeExtractor(),
        registry=FakeRegistry(),
    )

    episode = FakeEpisode([])

    facts = consolidator.consolidate(episode)

    assert facts == []


def test_consolidate_single_memory():

    registry = FakeRegistry()

    consolidator = MemoryConsolidator(
        extractor=FakeExtractor(),
        registry=registry,
    )

    episode = FakeEpisode([
        FakeMemory("User likes Python")
    ])

    facts = consolidator.consolidate(episode)

    assert len(facts) == 1
    assert registry.items == facts


def test_consolidate_multiple_memories():

    registry = FakeRegistry()

    consolidator = MemoryConsolidator(
        extractor=FakeExtractor(),
        registry=registry,
    )

    episode = FakeEpisode([
        FakeMemory("One"),
        FakeMemory("Two"),
        FakeMemory("Three"),
    ])

    facts = consolidator.consolidate(episode)

    assert len(facts) == 3
    assert len(registry.items) == 3


def test_consolidate_ignores_none():

    registry = FakeRegistry()

    consolidator = MemoryConsolidator(
        extractor=FakeExtractor(),
        registry=registry,
    )

    episode = FakeEpisode([
        FakeMemory("One"),
        FakeMemory("ignore"),
        FakeMemory("Three"),
    ])

    facts = consolidator.consolidate(episode)

    assert len(facts) == 2
    assert len(registry.items) == 2


def test_consolidate_none_episode():

    consolidator = MemoryConsolidator(
        extractor=FakeExtractor(),
        registry=FakeRegistry(),
    )

    facts = consolidator.consolidate(None)

    assert facts == []