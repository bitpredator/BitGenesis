from bitgenesis.reasoning.reflection_rules import (
    ReflectionRules,
)


class ReflectionEngine:

    def __init__(self, rules=None):

        self.rules = rules or ReflectionRules()

    def reflect(self, facts):

        if not facts:
            return []

        return self.rules.apply(facts)