from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState


class CognitiveLoop:
    """
    Executes the ordered sequence of cognitive processing stages.

    The loop is responsible for advancing the cognitive context
    through each stage of the pipeline.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        self._perceive(context)

        self._contextualize(context)

        self._retrieve_memory(context)

        self._integrate_knowledge(context)

        self._reason(context)

        self._plan(context)

        self._execute_actions(context)

        self._reflect(context)

        self._consolidate(context)

        context.update_state(CognitiveState.COMPLETED)

        return context

    def _perceive(self, context: CognitiveContext):

        context.update_state(CognitiveState.PERCEIVING)

    def _contextualize(self, context: CognitiveContext):

        context.update_state(CognitiveState.CONTEXTUALIZING)

    def _retrieve_memory(self, context: CognitiveContext):

        context.update_state(CognitiveState.RETRIEVING_MEMORY)

    def _integrate_knowledge(self, context: CognitiveContext):

        context.update_state(CognitiveState.INTEGRATING_KNOWLEDGE)

    def _reason(self, context: CognitiveContext):

        context.update_state(CognitiveState.REASONING)

    def _plan(self, context: CognitiveContext):

        context.update_state(CognitiveState.PLANNING)

    def _execute_actions(self, context: CognitiveContext):

        context.update_state(CognitiveState.EXECUTING)

    def _reflect(self, context: CognitiveContext):

        context.update_state(CognitiveState.REFLECTING)

    def _consolidate(self, context: CognitiveContext):

        context.update_state(CognitiveState.CONSOLIDATING)