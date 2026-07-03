from bitgenesis.reasoning.engine import ReasoningEngine
from bitgenesis.reasoning.context_fusion import ContextFusion
from bitgenesis.reasoning.context import ReasoningContext


class ReasoningSession:

    def __init__(self, memory_store):

        self.memory_store = memory_store

        self.engine = ReasoningEngine()
        self.fusion = ContextFusion()

    def process(self, event):

        unified = self.fusion.build(
            event=event,
            memory_store=self.memory_store,
        )

        context = ReasoningContext(unified=unified)

        return self.engine.evaluate(context)