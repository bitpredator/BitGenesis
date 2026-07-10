from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.stages.execution import ExecutionStage


class DummyExecutor:

    def execute(self, plan):

        return {
            "executed": plan
        }


def test_execution_stage_executes_plan():

    context = CognitiveContext()

    context.plan = {
        "action": "test"
    }

    context.executor = DummyExecutor()

    stage = ExecutionStage()

    result = stage.execute(
        context
    )

    assert result.response == {
        "executed": {
            "action": "test"
        }
    }


def test_execution_stage_without_executor():

    context = CognitiveContext()

    context.plan = {
        "action": "test"
    }

    stage = ExecutionStage()

    result = stage.execute(
        context
    )

    assert result.response is None