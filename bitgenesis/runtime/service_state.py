from __future__ import annotations

from enum import Enum


class ServiceState(Enum):
    """
    Runtime service lifecycle state.
    """

    CREATED = "created"

    REGISTERED = "registered"

    STARTING = "starting"

    READY = "ready"

    RUNNING = "running"

    STOPPING = "stopping"

    STOPPED = "stopped"

    FAILED = "failed"