from __future__ import annotations


from bitgenesis.language.context import (
    LanguageContext,
)


from bitgenesis.language.detector import (
    LanguageDetector,
)


from bitgenesis.language.tokenizer import (
    Tokenizer,
)


from bitgenesis.language.normalizer import (
    TextNormalizer,
)


from bitgenesis.language.intent_detector import (
    IntentDetector,
)


from bitgenesis.language.entity_extractor import (
    EntityExtractor,
)



class LanguageProcessor:
    """
    Coordinates the complete language pipeline.

    Pipeline:

    Raw text
        |
        v
    Normalization
        |
        v
    Tokenization
        |
        v
    Language detection
        |
        v
    Intent detection
        |
        v
    Entity extraction
        |
        v
    LanguageContext
    """



    def __init__(
        self,
        *,
        detector: LanguageDetector | None = None,
        tokenizer: Tokenizer | None = None,
        normalizer: TextNormalizer | None = None,
        intent_detector: IntentDetector | None = None,
        entity_extractor: EntityExtractor | None = None,
    ):


        self.detector = (
            detector
            or LanguageDetector()
        )


        self.tokenizer = (
            tokenizer
            or Tokenizer()
        )


        self.normalizer = (
            normalizer
            or TextNormalizer()
        )


        self.intent_detector = (
            intent_detector
            or IntentDetector()
        )


        self.entity_extractor = (
            entity_extractor
            or EntityExtractor()
        )



    def process(
        self,
        text: str,
    ) -> LanguageContext:
        """
        Processes raw input text.
        """


        # ----------------------------------------
        # Normalize
        # ----------------------------------------

        normalized = (
            self.normalizer.normalize(
                text
            )
        )



        # ----------------------------------------
        # Tokenization
        # ----------------------------------------

        tokens = (
            self.tokenizer.tokenize(
                normalized
            )
        )



        # ----------------------------------------
        # Language detection
        # ----------------------------------------

        language = (
            self.detector.detect(
                normalized
            )
        )



        # ----------------------------------------
        # Intent detection
        # ----------------------------------------

        intent = (
            self.intent_detector.detect(
                normalized,
                language=language,
            )
        )



        # ----------------------------------------
        # Entity extraction
        # ----------------------------------------

        entities = (
            self.entity_extractor.extract(
                normalized
            )
        )



        # ----------------------------------------
        # Context creation
        # ----------------------------------------

        return LanguageContext(

            raw_text=text,

            language=language,

            tokens=tokens,

            normalized_text=normalized,

            intent=intent,

            entities=entities,

            confidence=(
                1.0
                if language.value != "unknown"
                else 0.5
            ),

            metadata={
                "token_count": len(tokens),

                "entity_count": len(entities),

                "intent": intent.value,
            },
        )