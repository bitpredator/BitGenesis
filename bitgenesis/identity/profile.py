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