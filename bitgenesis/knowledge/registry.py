from __future__ import annotations

from bitgenesis.knowledge.entity_node import EntityNode
from bitgenesis.knowledge.fact import Fact


class KnowledgeRegistry:
    """
    Central registry for persistent structured knowledge.

    The registry stores:

    - entities
    - facts

    Entity handling remains backwards compatible with the
    original registry API.

    Facts are represented as structured Fact objects and can
    be added, queried and removed independently from entities.
    """

    def __init__(self):

        self._entities: dict[str, EntityNode] = {}

        self._facts: list[Fact] = []

    # ==================================================
    # Entities
    # ==================================================

    def get_or_create(
        self,
        name: str,
        entity_type: str = "generic",
        attributes: dict | None = None,
    ) -> EntityNode:
        """
        Returns an existing entity or creates a new one.
        """

        key = name.strip().lower()

        if key in self._entities:

            return self._entities[key]

        entity = EntityNode(
            name=name,
            entity_type=entity_type,
            attributes=attributes or {},
        )

        self._entities[key] = entity

        return entity

    def get(
        self,
        name: str,
    ) -> EntityNode | None:
        """
        Returns an entity by name.
        """

        return self._entities.get(
            name.strip().lower()
        )

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Returns True when an entity exists.
        """

        return (
            name.strip().lower()
            in self._entities
        )

    def all(self) -> list[EntityNode]:
        """
        Returns all registered entities.
        """

        return list(
            self._entities.values()
        )

    def count(self) -> int:
        """
        Returns the number of registered entities.
        """

        return len(
            self._entities
        )

    # ==================================================
    # Facts
    # ==================================================

    def add_fact(
        self,
        fact: Fact,
    ) -> Fact:
        """
        Adds a fact to the knowledge registry.

        Duplicate facts are ignored.

        The original Fact instance is returned.
        """

        if not isinstance(
            fact,
            Fact,
        ):
            raise TypeError(
                "fact must be a Fact instance"
            )

        if fact in self._facts:

            return fact

        self._facts.append(
            fact
        )

        return fact

    def add_fact_from_string(
        self,
        value: str,
    ) -> Fact:
        """
        Creates and registers a Fact from its textual form.

        Example:

            "BitGenesis created_by Bitpredator"
        """

        fact = Fact.from_string(
            value
        )

        return self.add_fact(
            fact
        )

    def facts(self) -> list[Fact]:
        """
        Returns all registered facts.
        """

        return list(
            self._facts
        )

    def fact_count(self) -> int:
        """
        Returns the number of registered facts.
        """

        return len(
            self._facts
        )

    def has_fact(
        self,
        fact: Fact,
    ) -> bool:
        """
        Returns True when the exact fact is registered.
        """

        return fact in self._facts

    def find_facts(
        self,
        *,
        subject: str | None = None,
        predicate: str | None = None,
        object: str | None = None,
    ) -> list[Fact]:
        """
        Searches registered facts.

        Any omitted parameter acts as a wildcard.

        Examples:

            find_facts(subject="BitGenesis")

            find_facts(predicate="created_by")

            find_facts(
                subject="BitGenesis",
                predicate="created_by",
            )
        """

        normalized_subject = (
            subject.strip().lower()
            if subject is not None
            else None
        )

        normalized_predicate = (
            predicate.strip().lower()
            if predicate is not None
            else None
        )

        normalized_object = (
            object.strip().lower()
            if object is not None
            else None
        )

        results = []

        for fact in self._facts:

            if (
                normalized_subject is not None
                and fact.subject.strip().lower()
                != normalized_subject
            ):
                continue

            if (
                normalized_predicate is not None
                and fact.predicate.strip().lower()
                != normalized_predicate
            ):
                continue

            if (
                normalized_object is not None
                and fact.object.strip().lower()
                != normalized_object
            ):
                continue

            results.append(
                fact
            )

        return results

    def remove_fact(
        self,
        fact: Fact,
    ) -> bool:
        """
        Removes a registered fact.

        Returns True when the fact existed and was removed.
        """

        if fact not in self._facts:

            return False

        self._facts.remove(
            fact
        )

        return True

    # ==================================================
    # Registry lifecycle
    # ==================================================

    def clear(self) -> None:
        """
        Clears both entities and facts.
        """

        self._entities.clear()

        self._facts.clear()