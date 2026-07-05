from dataclasses import dataclass


@dataclass(slots=True)
class Intent:

    domain: str
    action: str
    target: str | None = None
    confidence: float = 1.0


class IntentDetector:

    _IDENTITY_PATTERNS = {
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
    }

    def detect(self, text: str) -> Intent | None:

        if not text:
            return None

        normalized = text.strip().lower()

        for target, patterns in self._IDENTITY_PATTERNS.items():

            for pattern in patterns:

                if pattern in normalized:

                    return Intent(
                        domain="identity",
                        action="query",
                        target=target,
                        confidence=1.0,
                    )

        return None