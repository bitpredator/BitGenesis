from bitgenesis.runtime.actions.memory import store_memory
from bitgenesis.runtime.actions.knowledge import query_knowledge_graph
from bitgenesis.runtime.result import ActionResult


class DummyStep:

    action = "test_action"
    target = "test"



class DummyContext:

    step = DummyStep()

    memory_store = None

    graph = None



def test_store_memory_returns_action_result():

    result = store_memory(
        DummyContext()
    )

    assert isinstance(
        result,
        ActionResult,
    )

    assert result.success is False



def test_knowledge_action_returns_action_result():

    result = query_knowledge_graph(
        DummyContext()
    )

    assert isinstance(
        result,
        ActionResult,
    )

    assert result.success is False