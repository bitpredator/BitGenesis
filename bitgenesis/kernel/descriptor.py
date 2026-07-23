from dataclasses import dataclass


@dataclass
class ServiceDescriptor:

    name: str

    version: str = "1.0.0"

    priority: int = 100

    tags: tuple = ()

    auto_start: bool = True