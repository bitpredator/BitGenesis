"""
Base entity for BitGenesis domain objects.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .identifiers import generate_id


@dataclass(slots=True, kw_only=True)
class Entity:
    """
    Base class for all persistent domain entities.

    Every entity owns a globally unique identifier and
    lifecycle timestamps.
    """

    id: str = field(default_factory=generate_id)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def touch(self) -> None:
        """
        Update the modification timestamp.
        """
        self.updated_at = datetime.now(UTC)