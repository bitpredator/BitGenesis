from bitgenesis.knowledge.inference_rules import (
    InferenceRules,
)


class InferenceEngine:

    def __init__(self, rules=None):

        self.rules = rules or InferenceRules()

    def infer(self, facts):

        if not facts:
            return []

        return self.rules.apply(facts)