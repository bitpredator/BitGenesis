from bitgenesis.cognition.executor import CognitiveExecutor


def test_executor_creation():

    executor = CognitiveExecutor()

    assert executor is not None


def test_executor_returns_plan():

    executor = CognitiveExecutor()

    plan = {
        "action": "test"
    }

    result = executor.execute(plan)

    assert result == plan