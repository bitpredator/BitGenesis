from __future__ import annotations

import re


class TextNormalizer:
    """
    Normalizes natural language input.

    Responsibilities:

    - lowercase conversion
    - whitespace cleanup
    - punctuation normalization
    - repeated symbols reduction

    Keeps question semantics by preserving
    a single question mark.
    """



    def normalize(
        self,
        text: str,
    ) -> str:
        """
        Returns normalized text.
        """


        if not text:

            return ""



        # lowercase

        text = text.lower()



        # normalize spaces

        text = re.sub(
            r"\s+",
            " ",
            text,
        ).strip()



        # keep question intent
        # convert ??? / ?? / !!!! patterns

        text = re.sub(
            r"\?+",
            "?",
            text,
        )


        text = re.sub(
            r"!+",
            "",
            text,
        )


        # remove punctuation except ?

        text = re.sub(
            r"[^\w\sàèéìòù?]",
            "",
            text,
        )


        # remove spaces before ?

        text = re.sub(
            r"\s+\?",
            "?",
            text,
        )


        return text.strip()