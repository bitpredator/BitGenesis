from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class KnowledgeStage(CognitiveStage):
    """
    Integrates knowledge relevant to the current cognitive context.

    The stage coordinates the cognitive pipeline with the knowledge
    subsystem through the shared CognitiveContext.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Retrieves and integrates relevant knowledge.
        """

        context.update_state(
            CognitiveState.INTEGRATING_KNOWLEDGE
        )

        knowledge_registry = context.knowledge_registry

        # Knowledge subsystem not connected.
        if knowledge_registry is None:
            return context

        try:

            knowledge_items = []

            query_data = context.input_data

            # Preferred query interface
            query = getattr(
                knowledge_registry,
                "query",
                None,
            )

            if callable(query):

                knowledge_items = query(
                    query_data
                )

            else:

                all_knowledge = getattr(
                    knowledge_registry,
                    "all",
                    None,
                )

                if callable(all_knowledge):

                    knowledge_items = all_knowledge()

            if knowledge_items is None:
                knowledge_items = []

            for item in knowledge_items:

                context.add_knowledge(
                    item
                )

            return context

        except Exception:

            # Knowledge failures must not terminate
            # the cognitive execution cycle.
            return context