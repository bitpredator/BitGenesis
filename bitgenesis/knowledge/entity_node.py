from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class EntityNode:

    id: UUID = field(default_factory=uuid4)

    name: str = ""

    entity_type: str = "generic"

    attributes: dict = field(default_factory=dict)