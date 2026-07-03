from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Relation:

    id: UUID = field(default_factory=uuid4)

    source: UUID | None = None

    target: UUID | None = None

    relation_type: str = ""

    weight: float = 1.0