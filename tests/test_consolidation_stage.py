from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState
from bitgenesis.cognition.stages.consolidation import ConsolidationStage


class DummyMemoryStore:

    def __init__(self):

        self.items = []


    def add(self, item):

        self.items.append(item)


class DummyKnowledgeRegistry:

    def __init__(self):

        self.items = []


    def add(self, item):

        self.items.append(item)


def test_consolidation_stage_completes_cycle():

    context = CognitiveContext()

    stage = ConsolidationStage()

    result = stage.execute(
        context
    )

    assert result.state == CognitiveState.COMPLETED


def test_consolidation_stage_keeps_reflection_data():

    context = CognitiveContext()

    context.reflection = {
        "quality": "good"
    }

    stage = ConsolidationStage()

    result = stage.execute(
        context
    )

    assert result.reflection == {
        "quality": "good"
    }

def test_consolidation_stores_memory():

    context = CognitiveContext()

    store = DummyMemoryStore()

    context.memory_store = store

    context.response = "answer"

    stage = ConsolidationStage()

    stage.execute(context)

    assert len(store.items) == 1

def test_consolidation_updates_knowledge():

    context = CognitiveContext()

    registry = DummyKnowledgeRegistry()

    context.knowledge_registry = registry

    stage = ConsolidationStage()

    stage.execute(context)

    assert len(registry.items) == 1    