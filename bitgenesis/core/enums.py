"""
Core enumerations shared across multiple BitGenesis modules.
"""

from enum import Enum


class LifecycleStatus(Enum):
    """
    Generic lifecycle state for executable or stateful objects.
    """

    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"