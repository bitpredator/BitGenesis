from bitgenesis.memory.importance import MemoryImportance


class FakeMemory:

    def __init__(self, message):

        self.content = {
            "payload": {
                "message": message
            }
        }


def test_importance_user_memory():

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory("User likes Python")
    )

    assert score == 0.95


def test_importance_planner_memory():

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory("Planner initialized")
    )

    assert score == 0.70


def test_importance_system_started():

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory("System started")
    )

    assert score == 0.40


def test_importance_generic_memory():

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory("Hello world")
    )

    assert score == 0.20


def test_importance_empty_message():

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory("")
    )

    assert score == 0.20


def test_importance_missing_message():

    class FakeMemory:

        content = {
            "payload": {}
        }

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory()
    )

    assert score == 0.20


def test_importance_invalid_message():

    class FakeMemory:

        content = {
            "payload": {
                "message": None
            }
        }

    evaluator = MemoryImportance()

    score = evaluator.score(
        FakeMemory()
    )

    assert score == 0.0