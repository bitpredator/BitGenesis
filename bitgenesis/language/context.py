from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


from bitgenesis.language.detector import Language
from bitgenesis.language.intent import Intent
from bitgenesis.language.entity import Entity



@dataclass(slots=True)
class LanguageContext:
    """
    Represents the result of language processing.

    Stores linguistic information generated
    before entering the cognitive pipeline.

    Contains:

    - detected language
    - tokens
    - normalized text
    - detected intent
    - extracted entities
    - linguistic metadata

    Future extensions:

    - semantic embeddings
    - sentiment analysis
    - entity linking
    - semantic memory integration
    """



    # --------------------------------------------------
    # Raw linguistic data
    # --------------------------------------------------

    raw_text: str

    language: Language

    tokens: list[str]

    normalized_text: str



    # --------------------------------------------------
    # Natural Language Understanding
    # --------------------------------------------------

    intent: Intent = Intent.UNKNOWN


    entities: list[Entity] = field(
        default_factory=list
    )


    confidence: float = 1.0



    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )



    # --------------------------------------------------
    # Properties
    # --------------------------------------------------

    @property
    def token_count(
        self,
    ) -> int:

        return len(
            self.tokens
        )



    @property
    def entity_count(
        self,
    ) -> int:

        return len(
            self.entities
        )



    # --------------------------------------------------
    # Entity helpers
    # --------------------------------------------------

    def add_entity(
        self,
        entity: Entity,
    ) -> None:

        self.entities.append(
            entity
        )



    # --------------------------------------------------
    # Serialization
    # --------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:
        """
        Returns serializable representation.
        """

        return {

            "raw_text": self.raw_text,

            "language": self.language.value,

            "tokens": self.tokens,

            "normalized_text": self.normalized_text,


            "intent": (
                self.intent.value
                if isinstance(
                    self.intent,
                    Intent,
                )
                else str(self.intent)
            ),


            "entities": [
                entity.to_dict()
                for entity in self.entities
            ],


            "confidence": self.confidence,


            "metadata": self.metadata,


            "created_at": (
                self.created_at.isoformat()
            ),
        }