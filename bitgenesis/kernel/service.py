from __future__ import annotations

from abc import ABC


class KernelService(ABC):
    """
    Base lifecycle contract for all BitGenesis runtime services.

    Every service managed by the Kernel must implement
    this lifecycle interface.
    """


    def start(self) -> None:
        """
        Called when the Kernel starts the service.
        """
        pass


    def stop(self) -> None:
        """
        Called when the Kernel stops the service.
        """
        pass


    def tick(self) -> None:
        """
        Called during Kernel runtime cycles.
        """
        pass