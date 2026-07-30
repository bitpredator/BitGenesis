from __future__ import annotations

from bitgenesis.dialogue.response import CognitiveResponse
from bitgenesis.dialogue.formatter import ResponseFormatter
from bitgenesis.reasoning.intent_detector import IntentDetector
from bitgenesis.reasoning.resolver import Resolver


class ResponseEngine:
    """
    Generates structured cognitive responses.

    The ResponseEngine converts internal reasoning results
    into a structured output usable by the cognitive runtime.

    It does not own cognition.
    It only transforms cognitive results into communication.
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


    def respond(
        self,
        question: str,
    ) -> CognitiveResponse | None:
        """
        Generates a cognitive response from an input question.
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


        content = self.formatter.format(
            resolution
        )


        return CognitiveResponse(
            content=content,
            confidence=1.0,
            intent=intent,
            reasoning_trace=[
                {
                    "resolver": resolution,
                }
            ],
        )