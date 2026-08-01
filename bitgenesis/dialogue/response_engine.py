from __future__ import annotations

from bitgenesis.dialogue.response import CognitiveResponse
from bitgenesis.dialogue.formatter import ResponseFormatter

from bitgenesis.reasoning.intent_detector import Intent
from bitgenesis.reasoning.intent_detector import IntentDetector

from bitgenesis.reasoning.resolution import Resolution
from bitgenesis.reasoning.resolver import Resolver


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
    ):

        self.detector = IntentDetector()

        self.resolver = Resolver(
            memory_store=memory_store
        )

        self.formatter = ResponseFormatter()


    # ==================================================
    # Public API
    # ==================================================

    def respond(
        self,
        question: str,
    ) -> CognitiveResponse | None:
        """
        Generates a structured response from user input.
        """


        intent = self.detector.detect(
            question
        )


        if intent is None:

            return None


        resolution = self.resolver.resolve(
            intent
        )


        if resolution is None:

            return None


        return self.respond_from_resolution(
            intent,
            resolution,
        )


    # ==================================================
    # Response generation
    # ==================================================

    def respond_from_resolution(
        self,
        intent: Intent,
        resolution: Resolution,
    ) -> CognitiveResponse:
        """
        Converts a resolved cognitive result into
        a structured response.
        """


        content = self.formatter.format(
            resolution
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