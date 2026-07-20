from __future__ import annotations

from abc import ABC


class KernelService(ABC):
    """
    Base lifecycle contract for every Kernel service.

    Services may override every method.
    """

    name = None

    version = "0.1.0"

    enabled = True


    @property
    def service_name(self) -> str:

        return self.name or self.__class__.__name__


    def metadata(self) -> dict:

        return {
            "name": self.service_name,
            "version": self.version,
            "enabled": self.enabled,
        }


    def start(self) -> None:
        pass


    def stop(self) -> None:
        pass


    def tick(self) -> None:
        pass