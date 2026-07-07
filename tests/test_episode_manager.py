from bitgenesis.memory.episode.manager import EpisodeManager


class FakeMemory:

    def __init__(
        self,
        category="system",
        importance=0.5,
        message="Memory",
    ):

        self.importance = importance

        self.content = {
            "event": {
                "category": category,
            },
            "payload": {
                "message": message,
            },
        }


def test_manager_creates_first_episode():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            message="System started",
        )
    )

    assert manager.count() == 1
    assert manager.current() is not None


def test_manager_keeps_same_episode():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            category="system",
            message="System started",
        )
    )

    manager.add(
        FakeMemory(
            category="system",
            message="Memory ready",
        )
    )

    assert manager.count() == 1
    assert len(manager.current().memories) == 2


def test_manager_starts_new_episode():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            category="system",
            message="System started",
        )
    )

    manager.add(
        FakeMemory(
            category="user",
            message="User likes Python",
        )
    )

    assert manager.count() == 2
    assert len(manager.all()) == 2


def test_manager_returns_current_episode():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            message="System started",
        )
    )

    episode = manager.current()

    assert episode is not None


def test_manager_returns_all_episodes():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            category="system",
            message="A",
        )
    )

    manager.add(
        FakeMemory(
            category="user",
            message="B",
        )
    )

    episodes = manager.all()

    assert len(episodes) == 2


def test_manager_count():

    manager = EpisodeManager()

    assert manager.count() == 0

    manager.add(FakeMemory())

    assert manager.count() == 1


def test_manager_clear():

    manager = EpisodeManager()

    manager.add(FakeMemory())

    manager.clear()

    assert manager.count() == 0
    assert manager.current() is None


def test_manager_updates_episode_importance():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            importance=0.2,
            message="First",
        )
    )

    manager.add(
        FakeMemory(
            importance=0.9,
            message="Second",
        )
    )

    assert manager.current().importance == 0.9


def test_manager_updates_episode_title():

    manager = EpisodeManager()

    manager.add(
        FakeMemory(
            message="Planner initialized",
        )
    )

    manager.add(
        FakeMemory(
            message="Planner ready",
        )
    )

    assert manager.current().title == "Planner Episode"