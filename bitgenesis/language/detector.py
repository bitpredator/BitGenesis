from __future__ import annotations

import re

from enum import Enum



class Language(Enum):
    """
    Supported languages detected by BitGenesis.
    """

    ITALIAN = "it"

    ENGLISH = "en"

    UNKNOWN = "unknown"




class LanguageDetector:
    """
    Basic language detector.

    This is intentionally lightweight.

    Future versions may replace this with:
    - statistical language models
    - neural language detection
    - multilingual embeddings
    """


    ITALIAN_MARKERS = {
        "il",
        "lo",
        "la",
        "gli",
        "le",
        "un",
        "una",
        "che",
        "chi",
        "cosa",
        "come",
        "perché",
        "perche",
        "sei",
        "creato",
        "creatore",
        "io",
        "tu",
    }


    ENGLISH_MARKERS = {
        "the",
        "a",
        "an",
        "who",
        "what",
        "how",
        "why",
        "are",
        "you",
        "created",
        "creator",
        "i",
        "your",
    }



    def detect(
        self,
        text: str,
    ) -> Language:
        """
        Detects the most probable language.
        """


        if not text:

            return Language.UNKNOWN



        tokens = self._tokenize(
            text
        )


        italian_score = len(
            set(tokens)
            &
            self.ITALIAN_MARKERS
        )


        english_score = len(
            set(tokens)
            &
            self.ENGLISH_MARKERS
        )



        if italian_score > english_score:

            return Language.ITALIAN



        if english_score > italian_score:

            return Language.ENGLISH



        return Language.UNKNOWN





    def _tokenize(
        self,
        text: str,
    ) -> list[str]:
        """
        Internal lightweight tokenizer.
        """


        return [
            token.lower()
            for token in re.findall(
                r"\b[\wàèéìòù]+\b",
                text.lower(),
            )
        ]