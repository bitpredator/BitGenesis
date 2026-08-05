from __future__ import annotations

import re



class Tokenizer:
    """
    Basic linguistic tokenizer.

    Responsible for converting raw text into
    normalized tokens.

    Future extensions:

    - stemming
    - lemmatization
    - semantic tokens
    - multilingual rules
    """



    TOKEN_PATTERN = re.compile(
        r"[a-zàèéìòù0-9']+",
        re.IGNORECASE,
    )



    def tokenize(
        self,
        text: str,
    ) -> list[str]:
        """
        Converts text into normalized tokens.
        """


        if not text:

            return []



        normalized = (
            text
            .lower()
            .strip()
        )



        tokens = self.TOKEN_PATTERN.findall(
            normalized
        )



        return [
            token
            for token in tokens
            if token
        ]