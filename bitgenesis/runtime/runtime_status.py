from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class RuntimeStatus(str, Enum):
    """
    Runtime lifecycle states.
    """

    IDLE = "idle"
    RUNNING = "running"
    FAILED = "failed"


@dataclass
class RuntimeState:
    """
    Tracks runtime execution state.
    """

    status: RuntimeStatus = RuntimeStatus.IDLE

    started_at: datetime | None = None
    stopped_at: datetime | None = None

    cycles: int = 0

    errors: list[str] = field(
        default_factory=list
    )


    # compatibility with existing tests/API

    IDLE = RuntimeStatus.IDLE
    RUNNING = RuntimeStatus.RUNNING
    FAILED = RuntimeStatus.FAILED


    def mark_started(self):
        """
        Marks runtime as started.
        """

        self.status = RuntimeStatus.RUNNING

        self.started_at = datetime.now()


    def mark_stopped(self):
        """
        Marks runtime as stopped.
        """

        self.status = RuntimeStatus.IDLE

        self.stopped_at = datetime.now()


    def update_cycle(
        self,
        cycle: int,
    ):
        """
        Updates cycle counter.
        """

        self.cycles = cycle


    def register_error(
        self,
        error: str,
    ):
        """
        Registers runtime error.
        """

        self.status = RuntimeStatus.FAILED

        self.errors.append(error)


    def reset(self):
        """
        Reset runtime statistics.
        """

        self.status = RuntimeStatus.IDLE

        self.started_at = None
        self.stopped_at = None

        self.cycles = 0

        self.errors.clear()