from __future__ import annotations


class KernelService:
    """
    Base lifecycle contract for Kernel-managed services.
    """


    def start(self) -> None:
        """
        Called when the Kernel starts.
        """
        pass


    def stop(self) -> None:
        """
        Called when the Kernel stops.
        """
        pass


    def tick(self) -> None:
        """
        Called during Kernel runtime cycles.
        """
        pass