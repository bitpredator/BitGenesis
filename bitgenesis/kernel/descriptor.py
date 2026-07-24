from dataclasses import dataclass
from typing import Tuple, Type

from bitgenesis.kernel.service import KernelService



@dataclass
class ServiceDescriptor:
    """
    Metadata describing a Kernel service.
    """

    name: str

    version: str = "1.0.0"

    priority: int = 100

    tags: tuple = ()

    auto_start: bool = True

    dependencies: Tuple[
        Type[KernelService],
        ...
    ] = ()



    def requires(
        self,
        service_type: Type[KernelService],
    ) -> bool:

        return service_type in self.dependencies