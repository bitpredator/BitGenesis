from dataclasses import dataclass


@dataclass(slots=True)
class Intent:

    domain: str
    action: str
    target: str | None = None
    confidence: float = 1.0


class IntentDetector:

    _PATTERNS = {
        "identity": {
            "creator": (
                "who created you",
                "who is your creator",
                "who made you",
            ),
            "name": (
                "who are you",
                "what is your name",
                "your name",
            ),
            "project": (
                "what is your project",
                "project name",
            ),
            "version": (
                "what is your version",
                "version",
            ),
            "description": (
                "what are you",
                "describe yourself",
                "what do you do",
            ),
        },

        "memory": {
            "latest": (
                "latest memory",
                "last memory",
            ),
            "recent": (
                "what do you remember",
                "tell me what you remember",
                "recent memories",
                "show me your recent memories",
            ),
        },
    }

    def detect(self, text: str) -> Intent | None:

        if not text:
            return None

        normalized = text.strip().lower()

        for domain, targets in self._PATTERNS.items():

            for target, patterns in targets.items():

                for pattern in patterns:

                    if pattern in normalized:

                        return Intent(
                            domain=domain,
                            action="query",
                            target=target,
                            confidence=1.0,
                        )

        return None