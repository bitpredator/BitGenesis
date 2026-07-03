from bitgenesis.reasoning.decision import Decision
from bitgenesis.reasoning.context_rules import ContextAwareRules


class ReasoningEngine:

    def evaluate(self, context):

        event = context.unified.event
        memory = context.unified.memory_context
        knowledge = context.unified.knowledge_context

        # 1. PERCEPTION PRIORITY ASSOLUTA
        if getattr(event, "type", None) == "perception.event":

            return Decision(
                action="store_information",
                confidence=1.0,
                explanation="Perception events are stored for future reasoning.",
                data=event.payload,
            )

        # 2. SCORING COGNITIVO
        memory_score = ContextAwareRules.score_memory(memory)
        knowledge_score = ContextAwareRules.score_knowledge(knowledge)

        decision = ContextAwareRules.decide(memory_score, knowledge_score)

        # 3. EXECUTION
        if decision == "use_knowledge":

            return Decision(
                action="use_knowledge",
                confidence=knowledge_score,
                explanation="Knowledge graph has higher relevance score.",
                data=knowledge.get("relations"),
            )

        if decision == "use_memory":

            return Decision(
                action="use_memory",
                confidence=memory_score,
                explanation="Memory context is more relevant.",
                data=memory.get("items"),
            )

        return Decision(
            action="ignore",
            confidence=0.5,
            explanation="No relevant cognitive signal detected."
        )