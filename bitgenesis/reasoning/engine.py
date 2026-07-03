from bitgenesis.reasoning.decision import Decision


class ReasoningEngine:

    def evaluate(self, context):

        event = context.unified.event
        memory = context.unified.memory_context
        knowledge = context.unified.knowledge_context

        # -------------------------
        # RULE 1: PERCEPTION
        # -------------------------
        if getattr(event, "type", None) == "perception.event":

            return Decision(
                action="store_information",
                confidence=1.0,
                explanation="Perception events are stored for future reasoning.",
                data=event.payload,
            )

        # -------------------------
        # RULE 2: KNOWLEDGE PRIORITY
        # -------------------------
        if knowledge and knowledge.get("relations"):

            return Decision(
                action="use_knowledge",
                confidence=0.95,
                explanation="Knowledge graph contains relevant relations.",
                data=knowledge["relations"],
            )

        # -------------------------
        # RULE 3: MEMORY FALLBACK
        # -------------------------
        if memory and memory.get("items"):

            return Decision(
                action="use_memory",
                confidence=0.7,
                explanation=f"Using {len(memory['items'])} memory items.",
                data=memory["items"],
            )

        # -------------------------
        # DEFAULT
        # -------------------------
        return Decision(
            action="ignore",
            confidence=0.5,
            explanation="No reasoning rule matched."
        )