from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass


@dataclass(slots=True)
class IdentityProfile:
    """
    Static identity of BitGenesis.

    This represents facts about the system itself,
    not temporary runtime state.
    """

    name: str
    creator: str
    project: str
    version: str
    description: str

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Serialize the identity profile.
        """

        return asdict(self)

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "IdentityProfile":
        """
        Restore an identity profile from serialized data.
        """

        return cls(
            name=data["name"],
            creator=data["creator"],
            project=data["project"],
            version=data["version"],
            description=data["description"],
        )