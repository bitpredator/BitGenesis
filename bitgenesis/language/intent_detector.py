from __future__ import annotations

from bitgenesis.language.detector import Language
from bitgenesis.language.intent import Intent


class IntentDetector:
    """
    Rule-based intent detector.

    Determines the user's high-level intention
    using lightweight heuristics.

    Future versions may introduce:

    - confidence scores
    - multiple intents
    - contextual reasoning
    - semantic classifiers
    """

    GREETINGS = {
        "ciao",
        "salve",
        "buongiorno",
        "buonasera",
        "hello",
        "hi",
        "hey",
    }

    FAREWELLS = {
        "arrivederci",
        "addio",
        "ciao ciao",
        "bye",
        "goodbye",
        "see you",
    }

    HELP = {
        "help",
        "aiuto",
        "support",
    }

    CONFIRMATIONS = {
        "si",
        "sì",
        "yes",
        "ok",
        "okay",
        "certo",
    }

    NEGATIONS = {
        "no",
        "non",
        "never",
        "nope",
    }

    CREATOR_PATTERNS = (
        "chi ti ha creato",
        "chi ti ha sviluppato",
        "chi è il tuo creatore",
        "chi e il tuo creatore",
        "who created you",
        "who made you",
        "who is your creator",
    )

    IDENTITY_PATTERNS = (
        "chi sei",
        "come ti chiami",
        "what are you",
        "who are you",
    )

    QUESTION_WORDS_IT = {
        "chi",
        "cosa",
        "come",
        "quando",
        "dove",
        "quale",
        "quali",
        "perché",
        "perche",
    }

    QUESTION_WORDS_EN = {
        "who",
        "what",
        "where",
        "when",
        "why",
        "how",
        "which",
    }

    COMMAND_WORDS_IT = {
        "apri",
        "esegui",
        "mostra",
        "crea",
        "elimina",
        "salva",
        "ricorda",
    }

    COMMAND_WORDS_EN = {
        "open",
        "execute",
        "show",
        "create",
        "delete",
        "save",
        "remember",
    }

    def detect(
        self,
        text: str,
        *,
        language: Language = Language.UNKNOWN,
    ) -> Intent:
        """
        Detects the user's primary intent.
        """

        if not text:
            return Intent.UNKNOWN

        normalized = text.strip().lower()

        if normalized in self.GREETINGS:
            return Intent.GREETING

        if normalized in self.FAREWELLS:
            return Intent.FAREWELL

        if normalized in self.HELP:
            return Intent.HELP

        if normalized in self.CONFIRMATIONS:
            return Intent.CONFIRMATION

        if normalized in self.NEGATIONS:
            return Intent.NEGATION

        for pattern in self.CREATOR_PATTERNS:
            if pattern in normalized:
                return Intent.CREATOR_QUERY

        for pattern in self.IDENTITY_PATTERNS:
            if pattern in normalized:
                return Intent.IDENTITY_QUERY

        words = set(normalized.replace("?", "").split())

        if language == Language.ITALIAN:

            if words & self.COMMAND_WORDS_IT:
                return Intent.COMMAND

            if words & self.QUESTION_WORDS_IT:
                return Intent.INFORMATION_REQUEST

        elif language == Language.ENGLISH:

            if words & self.COMMAND_WORDS_EN:
                return Intent.COMMAND

            if words & self.QUESTION_WORDS_EN:
                return Intent.INFORMATION_REQUEST

        else:

            if normalized.endswith("?"):
                return Intent.QUESTION

        if normalized.endswith("?"):
            return Intent.QUESTION

        return Intent.STATEMENT