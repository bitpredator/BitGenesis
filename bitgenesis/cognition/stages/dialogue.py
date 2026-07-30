from __future__ import annotations

from bitgenesis.cognition.context import CognitiveContext


class DialogueStage:
    """
    Generates the final cognitive response.

    The DialogueStage represents the final communication
    phase of the cognitive cycle.

    Responsibilities:

    - consume cognitive results
    - invoke the response engine
    - attach generated response to context

    It does not perform reasoning.
    It only transforms internal cognitive state
    into an external response.
    """


    def execute(
        self,
        context: CognitiveContext,
    ) -> CognitiveContext:
        """
        Execute dialogue generation.
        """

        # --------------------------------------------------
        # Validate response engine availability
        # --------------------------------------------------

        if context.response_engine is None:

            return context


        # --------------------------------------------------
        # Generate response
        # --------------------------------------------------

        response = context.response_engine.respond(
            context.input_data
        )


        # --------------------------------------------------
        # Store result in cognitive context
        # --------------------------------------------------

        context.response = response


        return context