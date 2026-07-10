from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.stages.reflection import ReflectionStage


class DummyReflectionEngine:

    def reflect(self, data):

        return {
            "quality": "good",
            "data": data,
        }


def test_reflection_stage_generates_reflection():

    context = CognitiveContext()

    context.input_data = "hello"

    context.response = {
        "answer": "world"
    }

    context.reflection_engine = DummyReflectionEngine()

    stage = ReflectionStage()

    result = stage.execute(
        context
    )

    assert result.reflection is not None

    assert result.reflection["quality"] == "good"

    assert result.reflection["data"]["response"] == {
        "answer": "world"
    }


def test_reflection_stage_without_engine():

    context = CognitiveContext()

    context.response = "test"

    stage = ReflectionStage()

    result = stage.execute(
        context
    )

    assert result.reflection is None