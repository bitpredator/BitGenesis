from __future__ import annotations

from dataclasses import dataclass

from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor


@dataclass(slots=True)
class ServiceEntry:
    """
    Represents a registered Kernel service.

    A ServiceEntry binds together the runtime service instance
    and its immutable descriptor metadata.

    This object becomes the single source of truth used by the
    registry and the service manager.
    """

    service: KernelService
    descriptor: ServiceDescriptor

    @property
    def service_type(self) -> type[KernelService]:
        return type(self.service)

    @property
    def name(self) -> str:
        return self.descriptor.name

    @property
    def priority(self) -> int:
        return self.descriptor.priority

    @property
    def auto_start(self) -> bool:
        return self.descriptor.auto_start