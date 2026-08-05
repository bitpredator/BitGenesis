from __future__ import annotations


from bitgenesis.dialogue.response import CognitiveResponse
from bitgenesis.dialogue.formatter import ResponseFormatter


from bitgenesis.reasoning.intent_detector import (
    Intent,
    IntentDetector,
)

from bitgenesis.reasoning.resolution import Resolution
from bitgenesis.reasoning.resolver import Resolver


from bitgenesis.language.detector import Language



class ResponseEngine:
    """
    Generates structured cognitive responses.

    The ResponseEngine converts detected intent and
    resolved knowledge into a CognitiveResponse object.

    It is the final bridge between cognition and dialogue.
    """



    def __init__(
        self,
        memory_store=None,
        knowledge_registry=None,
    ):

        self.detector = IntentDetector()


        self.resolver = Resolver(

            memory_store=memory_store,

            knowledge_registry=knowledge_registry,

        )


        self.formatter = ResponseFormatter()



    # ==================================================
    # Public API
    # ==================================================


    def respond(
        self,
        question: str,
        language: Language | None = None,
    ) -> CognitiveResponse | None:
        """
        Generates a structured response from user input.

        The language parameter comes from the cognitive
        perception stage and controls response formatting.
        """



        if not question or not question.strip():

            return None



        intent = self.detector.detect(
            question
        )



        if intent is None:

            return self.unknown_response(
                language=language
            )



        resolution = self.resolver.resolve(
            intent
        )



        if resolution is None:

            return self.unknown_response(
                intent,
                language=language,
            )



        return self.respond_from_resolution(
            intent,
            resolution,
            language=language,
        )



    # ==================================================
    # Response generation
    # ==================================================


    def respond_from_resolution(
        self,
        intent: Intent,
        resolution: Resolution,
        language: Language | None = None,
    ) -> CognitiveResponse:
        """
        Converts a resolved cognitive result into
        a structured response.
        """



        content = self.formatter.format(

            resolution,

            language=language,

        )



        return CognitiveResponse(

            content=str(content),

            confidence=intent.confidence,

            intent=intent,

            reasoning_trace=[
                {
                    "resolution": resolution,
                }
            ],
        )



    # ==================================================
    # Unknown knowledge handling
    # ==================================================


    def unknown_response(
        self,
        intent=None,
        language: Language | None = None,
    ) -> CognitiveResponse:
        """
        Generates a cognitive fallback response.
        """



        if language == Language.ITALIAN:

            content = (
                "Non ho ancora abbastanza conoscenze "
                "su questo argomento. "
                "Questa esperienza potrebbe diventare "
                "parte del mio futuro processo di apprendimento."
            )

        else:

            content = (
                "I do not have enough knowledge "
                "about this subject yet. "
                "This experience could become "
                "part of my future learning process."
            )



        return CognitiveResponse(

            content=content,


            confidence=(

                intent.confidence

                if intent is not None

                else 0.0

            ),


            intent=intent,


            reasoning_trace=[
                {
                    "type": "unknown_knowledge",
                }
            ],
        )