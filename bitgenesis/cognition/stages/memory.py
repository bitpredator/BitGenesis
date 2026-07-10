from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class MemoryStage(CognitiveStage):
    """
    Retrieves relevant information from the memory subsystem.

    The stage coordinates the interaction between the cognitive
    pipeline and the memory subsystem through CognitiveContext.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Retrieves memories related to the current cognitive input.
        """

        context.update_state(
            CognitiveState.RETRIEVING_MEMORY
        )

        memory_store = context.memory_store

        # No memory subsystem connected
        if memory_store is None:
            return context

        try:

            memories = []

            input_data = context.input_data

            # Prefer dedicated retrieval
            retrieve = getattr(
                memory_store,
                "retrieve",
                None,
            )

            if callable(retrieve):

                memories = retrieve(
                    input_data
                )

            else:

                all_memories = getattr(
                    memory_store,
                    "all",
                    None,
                )

                if callable(all_memories):

                    memories = all_memories()

            if memories is None:
                memories = []

            for memory in memories:

                context.add_memory(
                    memory
                )

                context.working_memory.append(
                    memory
                )

            return context

        except Exception:

            # Memory subsystem failures must not
            # terminate the cognitive cycle.
            return context