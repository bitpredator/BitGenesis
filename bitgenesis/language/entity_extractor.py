from __future__ import annotations

import re

from bitgenesis.language.entity import (
    Entity,
    EntityType,
)


class EntityExtractor:
    """
    Rule-based entity extractor.

    Extracts simple semantic entities from text.

    Future versions may integrate:

    - KnowledgeRegistry
    - MemoryStore
    - Ontologies
    - Named Entity Recognition
    - Semantic embeddings
    """

    PROJECTS = {
        "bitgenesis",
    }

    SERVICES = {
        "github",
        "git",
        "discord",
        "python",
    }

    LANGUAGES = {
        "italiano",
        "italian",
        "inglese",
        "english",
        "francese",
        "french",
    }

    TOOLS = {
        "chatgpt",
        "vscode",
        "visual studio code",
    }

    MEMORY_KEYWORDS = {
        "memoria",
        "memory",
    }

    KNOWLEDGE_KEYWORDS = {
        "conoscenza",
        "knowledge",
    }

    def extract(
        self,
        text: str,
    ) -> list[Entity]:
        """
        Extracts entities from text.
        """

        if not text:
            return []

        entities: list[Entity] = []

        normalized = text.lower()

        words = re.findall(
            r"\b[\wàèéìòù]+\b",
            normalized,
        )

        seen: set[tuple[EntityType, str]] = set()

        def add(
            entity_type: EntityType,
            value: str,
            confidence: float = 1.0,
        ) -> None:

            key = (
                entity_type,
                value.lower(),
            )

            if key in seen:
                return

            seen.add(key)

            entities.append(
                Entity(
                    type=entity_type,
                    value=value,
                    confidence=confidence,
                )
            )

        # ----------------------------------------
        # Projects
        # ----------------------------------------

        for project in self.PROJECTS:

            if project in normalized:

                add(
                    EntityType.PROJECT,
                    project,
                )

        # ----------------------------------------
        # Services
        # ----------------------------------------

        for service in self.SERVICES:

            if service in normalized:

                add(
                    EntityType.SERVICE,
                    service,
                )

        # ----------------------------------------
        # Languages
        # ----------------------------------------

        for language in self.LANGUAGES:

            if language in normalized:

                add(
                    EntityType.LANGUAGE,
                    language,
                )

        # ----------------------------------------
        # Tools
        # ----------------------------------------

        for tool in self.TOOLS:

            if tool in normalized:

                add(
                    EntityType.TOOL,
                    tool,
                )

        # ----------------------------------------
        # Memory
        # ----------------------------------------

        for keyword in self.MEMORY_KEYWORDS:

            if keyword in normalized:

                add(
                    EntityType.MEMORY,
                    keyword,
                )

        # ----------------------------------------
        # Knowledge
        # ----------------------------------------

        for keyword in self.KNOWLEDGE_KEYWORDS:

            if keyword in normalized:

                add(
                    EntityType.KNOWLEDGE,
                    keyword,
                )

        # ----------------------------------------
        # Numbers
        # ----------------------------------------

        for word in words:

            if word.isdigit():

                add(
                    EntityType.NUMBER,
                    word,
                )

        return entities