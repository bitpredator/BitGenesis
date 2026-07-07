from bitgenesis.memory.episode.builder import EpisodeBuilder


class FakeMemory:

    def __init__(self, importance, message=""):

        self.importance = importance

        self.content = {
            "payload": {
                "message": message
            }
        }


def test_builder_creates_episode():

    builder = EpisodeBuilder()

    episode = builder.build([])

    assert episode is not None


def test_builder_contains_memories():

    builder = EpisodeBuilder()

    memories = [
        FakeMemory(0.2, "Planner initialized"),
        FakeMemory(0.8, "Planner ready"),
    ]

    episode = builder.build(memories)

    assert len(episode.memories) == 2


def test_builder_uses_max_importance():

    builder = EpisodeBuilder()

    memories = [
        FakeMemory(0.2, "A"),
        FakeMemory(0.5, "B"),
        FakeMemory(0.9, "C"),
    ]

    episode = builder.build(memories)

    assert episode.importance == 0.9


def test_builder_empty_episode_importance():

    builder = EpisodeBuilder()

    episode = builder.build([])

    assert episode.importance == 0.0