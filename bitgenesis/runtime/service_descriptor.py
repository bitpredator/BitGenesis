from __future__ import annotations

from dataclasses import dataclass
from typing import Any



@dataclass(frozen=True)
class ServiceDescriptor:
    """
    Describes a runtime service.

    Used for service discovery.

    Contains:
    - service name
    - service instance
    - metadata
    """


    name: str

    service: object

    metadata: dict[str, Any] | None = None



    def get(
        self,
        key: str,
        default=None,
    ):
        """
        Read metadata value.
        """

        if not self.metadata:
            return default

        return self.metadata.get(
            key,
            default,
        )