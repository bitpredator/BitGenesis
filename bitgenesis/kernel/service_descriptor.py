from __future__ import annotations


class ServiceDescriptor:
    """
    Metadata and configuration descriptor for kernel services.
    """

    def __init__(
        self,
        name: str | None = None,
        version: str = "1.0.0",
        priority: int = 100,
        tags: tuple[str, ...] = (),
        dependencies: tuple[type, ...] = (),
        auto_start: bool = True,
        enabled: bool = True,
    ):

        self.name = name
        self.version = version
        self.priority = priority
        self.tags = tags
        self.dependencies = dependencies
        self.auto_start = auto_start
        self.enabled = enabled