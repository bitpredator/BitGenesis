from bitgenesis.reasoning.decision import Decision


class MemoryRule:

    def evaluate(self, context):

        if context.memory_context is None:
            return None

        memories = context.memory_context.get("items", [])

        if not memories:
            return None

        return Decision(
            action="use_memory",
            confidence=0.90,
            explanation=f"Found {len(memories)} relevant memories.",
            data=memories,
        )