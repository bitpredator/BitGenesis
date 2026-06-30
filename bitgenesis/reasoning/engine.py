from bitgenesis.reasoning.context import ReasoningContext
from bitgenesis.reasoning.decision import Decision


class ReasoningEngine:

    def evaluate(self, context: ReasoningContext) -> Decision:

        event = context.event

        if event.type == "perception.event":

            return Decision(
                action="store_information",
                confidence=1.0,
                explanation="Perception events are stored for future reasoning.",
                data=event.payload,
            )

        return Decision(
            action="ignore",
            confidence=0.5,
            explanation="No reasoning rule matched."
        )