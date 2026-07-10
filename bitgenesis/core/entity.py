from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid4


@dataclass(slots=True)
class Entity:
    """
    Base identity object for all system entities.
    """

    id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def touch(self) -> None:
        """
        Update the last modification timestamp safely.
        Ensures monotonic time progression.
        """
        now = datetime.now(UTC)

        if now <= self.updated_at:
            now = self.updated_at.replace(
                microsecond=self.updated_at.microsecond + 1
            )

        self.updated_at = now

    def to_dict(self) -> dict:
        """
        Serialize entity into a JSON-compatible dictionary.
        """

        return {
            "id": str(self.id),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }