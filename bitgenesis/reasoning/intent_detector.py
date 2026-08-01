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


    _MEMORY_QUERY_PATTERNS = {
        "latest": (
            "what is your latest memory",
            "what was your latest memory",
        ),
        "recent": (
            "show me your recent memories",
            "what do you remember",
            "tell me what you remember",
        ),
    }


    def detect(
        self,
        text: str
    ) -> Intent | None:


        if not text:

            return None


        normalized = text.strip().lower()


        if not normalized:

            return None


        # --------------------------
        # MEMORY SEARCH
        # --------------------------

        if "remember about" in normalized:

            target = normalized.split(
                "remember about",
                1
            )[1].strip()


            if target:

                return Intent(
                    domain="memory",
                    action="search",
                    target=target.rstrip("?"),
                    confidence=1.0,
                )


        if normalized.startswith(
            "do you remember "
        ):

            target = normalized.replace(
                "do you remember ",
                "",
                1
            ).strip()


            if target:

                return Intent(
                    domain="memory",
                    action="search",
                    target=target.rstrip("?"),
                    confidence=1.0,
                )


        # --------------------------
        # MEMORY QUERY
        # --------------------------

        for target, patterns in self._MEMORY_QUERY_PATTERNS.items():

            for pattern in patterns:

                if pattern in normalized:

                    return Intent(
                        domain="memory",
                        action="query",
                        target=target,
                        confidence=1.0,
                    )


        # --------------------------
        # IDENTITY
        # --------------------------

        for target, patterns in self._IDENTITY_PATTERNS.items():

            for pattern in patterns:

                if pattern in normalized:

                    return Intent(
                        domain="identity",
                        action="query",
                        target=target,
                        confidence=1.0,
                    )


        # --------------------------
        # UNKNOWN KNOWLEDGE
        # --------------------------

        return Intent(
            domain="unknown",
            action="unknown",
            target=text,
            confidence=0.0,
        )