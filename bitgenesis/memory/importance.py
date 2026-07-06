class MemoryImportance:

    def __init__(self):

        self._keywords = {
            "user": 0.95,
            "remember": 0.90,
            "preference": 0.90,
            "important": 0.90,
            "python": 0.80,
            "planner": 0.70,
            "error": 0.70,
            "warning": 0.70,
            "started": 0.40,
            "initialized": 0.40,
        }

    def score(self, memory):

        message = (
            memory.content
            .get("payload", {})
            .get("message", "")
        )

        if not isinstance(message, str):
            return 0.0

        text = message.lower()

        score = 0.20

        for keyword, weight in self._keywords.items():

            if keyword in text:
                score = max(score, weight)

        return min(score, 1.0)