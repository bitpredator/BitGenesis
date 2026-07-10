from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class ConsolidationStage(CognitiveStage):
    """
    Consolidates the results of a completed cognitive cycle.

    The stage coordinates final persistence, event notification
    and cycle completion without implementing subsystem logic.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Finalizes the cognitive execution cycle.
        """

        context.update_state(
            CognitiveState.CONSOLIDATING
        )

        try:

            # -------------------------------------------------
            # Memory consolidation
            # -------------------------------------------------

            memory_store = context.memory_store

            if memory_store is not None:

                if hasattr(memory_store, "consolidate"):

                    memory_store.consolidate(
                        context
                    )


            # -------------------------------------------------
            # Event notification
            # -------------------------------------------------

            event_bus = context.event_bus

            if event_bus is not None:

                if hasattr(event_bus, "publish"):

                    event_bus.publish(
                        "cognitive_cycle_completed",
                        context,
                    )


            # -------------------------------------------------
            # Final state
            # -------------------------------------------------

            context.update_state(
                CognitiveState.COMPLETED
            )

            return context

        except Exception:

            # Consolidation failures must not destroy
            # the completed cognitive result.

            context.update_state(
                CognitiveState.COMPLETED
            )

            return context