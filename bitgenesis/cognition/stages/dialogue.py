from __future__ import annotations


from bitgenesis.cognition.context import CognitiveContext



class DialogueStage:
    """
    Generates the final cognitive response.

    Final communication layer of the cognitive pipeline.

    The stage forwards language context detected during
    perception to the dialogue system.
    """



    def execute(
        self,
        context: CognitiveContext,
    ) -> CognitiveContext:


        if context.response_engine is None:

            return context



        # Always use original input.
        #
        # Reasoning output is internal cognitive data,
        # not a user question.

        dialogue_input = context.input_data



        language = None


        if context.language_context is not None:

            language = (
                context.language_context.language
            )



        response = context.response_engine.respond(

            dialogue_input,

            language=language,

        )



        context.response = response


        return context