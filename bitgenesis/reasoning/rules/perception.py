from bitgenesis.reasoning.decision import Decision


class PerceptionRule:

    def evaluate(self, context):

        event = context.event

        if event.type != "perception.event":
            return None

        return Decision(
            action="store_information",
            confidence=1.0,
            explanation="Perception events are stored for future reasoning.",
            data=event.payload,
        )