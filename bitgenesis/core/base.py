"""
Base object definition used by every Core Object.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .identifiers import CoreID, generate_id
from .metadata import Metadata
from .serialization import Serializable


@dataclass(frozen=True, slots=True)
class BaseObject(Serializable):
    """
    Root class for every BitGenesis Core Object.
    """

    id: CoreID = field(default_factory=generate_id)
    metadata: Metadata = field(default_factory=Metadata)

    def validate(self) -> None:
        """
        Placeholder for future validation.
        """
        return