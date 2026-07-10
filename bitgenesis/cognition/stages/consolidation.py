from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory
from bitgenesis.events.enums import EventType

from .base import CognitiveStage


class ConsolidationStage(CognitiveStage):
    """
    Finalizes the cognitive cycle.

    Consolidation delegates persistence to the existing
    memory and knowledge subsystems.
    """

    def execute(
        self,
        context: CognitiveContext
    ) -> CognitiveContext:

        context.update_state(
            CognitiveState.CONSOLIDATING
        )

        try:

            consolidated_data = {
                "input": context.input_data,
                "response": context.response,
                "reflection": context.reflection,
            }

            # -----------------------------
            # Memory consolidation
            # -----------------------------

            memory_store = context.memory_store

            if memory_store is not None:

                memory_object = consolidated_data

                if context.memory_factory is not None:

                    event = Event(
                        category=EventCategory.MEMORY,
                        type=EventType.MEMORY_CREATED,
                        source="cognitive_runtime",
                        payload=consolidated_data,
                    )

                    memory_object = (
                        context.memory_factory
                        .from_event(event)
                    )

                if hasattr(memory_store, "add"):

                    memory_store.add(
                        memory_object
                    )

            # -----------------------------
            # Knowledge consolidation
            # -----------------------------

            knowledge_registry = (
                context.knowledge_registry
            )

            if knowledge_registry is not None:

                if hasattr(
                    knowledge_registry,
                    "add"
                ):

                    knowledge_registry.add(
                        consolidated_data
                    )

            return context

        finally:

            context.update_state(
                CognitiveState.COMPLETED
            )