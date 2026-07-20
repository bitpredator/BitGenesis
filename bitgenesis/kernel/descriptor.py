from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ServiceDescriptor:
    """
    Describes a Kernel service.

    The descriptor contains static metadata used
    by the Kernel to discover, validate and order
    services before startup.
    """

    name: str

    version: str = "1.0.0"

    priority: int = 100

    auto_start: bool = True

    dependencies: tuple[str, ...] = field(
        default_factory=tuple
    )

    tags: tuple[str, ...] = field(
        default_factory=tuple
    )