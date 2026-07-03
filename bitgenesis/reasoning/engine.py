from bitgenesis.reasoning.decision import Decision

from bitgenesis.reasoning.rules.perception import PerceptionRule
from bitgenesis.reasoning.rules.identity import IdentityRule
from bitgenesis.reasoning.rules.memory import MemoryRule


class ReasoningEngine:

    def __init__(self):

        self.rules = [
            PerceptionRule(),
            IdentityRule(),
            MemoryRule(),
        ]

    def evaluate(self, context):

        for rule in self.rules:

            decision = rule.evaluate(context)

            if decision is not None:
                return decision

        return Decision(
            action="ignore",
            confidence=0.5,
            explanation="No reasoning rule matched.",
        )