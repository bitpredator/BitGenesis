from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Fact:
    """
    Represents a single piece of structured knowledge.

    A fact is composed of:

    subject
    predicate
    object

    Example:

        Fact(
            subject="BitGenesis",
            predicate="created_by",
            object="Bitpredator",
        )

    String representation remains compatible with the
    existing three-part fact format.
    """

    subject: str

    predicate: str

    object: str

    def __str__(self) -> str:
        """
        Returns the textual representation of the fact.
        """

        return (
            f"{self.subject} "
            f"{self.predicate} "
            f"{self.object}"
        )

    @classmethod
    def from_string(
        cls,
        value: str,
    ) -> "Fact":
        """
        Creates a Fact from the existing textual format.

        Example:

            "Python is_a ProgrammingLanguage"

        becomes:

            Fact(
                subject="Python",
                predicate="is_a",
                object="ProgrammingLanguage",
            )
        """

        parts = value.strip().split()

        if len(parts) != 3:
            raise ValueError(
                "A fact must contain exactly "
                "three components: subject, predicate, object."
            )

        return cls(
            subject=parts[0],
            predicate=parts[1],
            object=parts[2],
        )