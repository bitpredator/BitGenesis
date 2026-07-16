"""
Kernel state definitions.

Compatibility layer for BitGenesis kernel lifecycle.
"""

from enum import Enum


class KernelState(str, Enum):
    """
    Current state of the BitGenesis Kernel.
    """

    CREATED = "created"

    READY = "ready"

    RUNNING = "running"

    STOPPED = "stopped"


__all__ = [
    "KernelState",
]