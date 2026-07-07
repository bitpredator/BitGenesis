from bitgenesis.memory.episode.title_generator import (
    EpisodeTitleGenerator,
)


class FakeMemory:

    def __init__(self, message):

        self.content = {
            "payload": {
                "message": message
            }
        }


def test_empty_episode():

    generator = EpisodeTitleGenerator()

    assert generator.generate([]) == "Empty Episode"


def test_system_episode():

    generator = EpisodeTitleGenerator()

    memories = [
        FakeMemory("System started"),
        FakeMemory("Memory subsystem ready"),
    ]

    assert generator.generate(memories) == "System Startup"


def test_planner_episode():

    generator = EpisodeTitleGenerator()

    memories = [
        FakeMemory("Planner initialized"),
    ]

    assert generator.generate(memories) == "Planner Episode"


def test_user_episode():

    generator = EpisodeTitleGenerator()

    memories = [
        FakeMemory("User likes Python"),
    ]

    assert generator.generate(memories) == "User Preferences"


def test_default_episode():

    generator = EpisodeTitleGenerator()

    memories = [
        FakeMemory("Coffee is ready"),
    ]

    assert generator.generate(memories) == "General Episode"