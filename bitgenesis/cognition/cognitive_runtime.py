from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState


class CognitiveRuntime:
    """
    Coordinates a single cognitive execution cycle.

    The runtime owns the execution flow while the individual
    cognitive subsystems remain responsible for their own logic.
    """

    def __init__(self):

        self.state = CognitiveState.IDLE

    @property
    def is_running(self) -> bool:

        return self.state != CognitiveState.IDLE

    def run(self, input_data=None) -> CognitiveContext:
        """
        Executes one cognitive cycle.

        Parameters
        ----------
        input_data:
            Initial input passed into the cognitive pipeline.
        """

        context = CognitiveContext(
            state=CognitiveState.INITIALIZING,
            input_data=input_data,
        )

        self.state = CognitiveState.INITIALIZING

        try:

            context.update_state(CognitiveState.PERCEIVING)

            context.update_state(CognitiveState.CONTEXTUALIZING)

            context.update_state(CognitiveState.COMPLETED)

            return context

        except Exception:

            context.update_state(CognitiveState.FAILED)

            raise

        finally:

            self.state = CognitiveState.IDLE