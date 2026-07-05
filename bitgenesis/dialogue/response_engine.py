from bitgenesis.dialogue.formatter import ResponseFormatter
from bitgenesis.reasoning.intent_detector import IntentDetector
from bitgenesis.reasoning.resolver import Resolver


class ResponseEngine:

    def __init__(self):

        self.detector = IntentDetector()
        self.resolver = Resolver()
        self.formatter = ResponseFormatter()

    def respond(self, question: str):

        intent = self.detector.detect(question)

        if intent is None:
            return None

        resolution = self.resolver.resolve(intent)

        return self.formatter.format(resolution)