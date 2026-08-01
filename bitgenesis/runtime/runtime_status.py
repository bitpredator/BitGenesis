from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum


class RuntimeStatus(str, Enum):
    """
    Runtime lifecycle states.
    """

    CREATED = "created"

    INITIALIZING = "initializing"

    IDLE = "idle"

    RUNNING = "running"

    STOPPING = "stopping"

    FAILED = "failed"


@dataclass
class RuntimeState:
    """
    Tracks runtime lifecycle and execution state.

    The RuntimeState is the central lifecycle record
    for the cognitive runtime.

    Responsibilities:

    - runtime status tracking
    - lifecycle timestamps
    - execution counters
    - error tracking
    - service tracking
    """


    status: RuntimeStatus = RuntimeStatus.CREATED


    # -------------------------------------------------
    # Lifecycle timestamps
    # -------------------------------------------------

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        )
    )

    started_at: datetime | None = None

    stopped_at: datetime | None = None


    # -------------------------------------------------
    # Execution metrics
    # -------------------------------------------------

    cycles: int = 0


    errors: list[str] = field(
        default_factory=list
    )


    # -------------------------------------------------
    # Service integration
    # -------------------------------------------------

    services: dict[str, str] = field(
        default_factory=dict
    )


    # -------------------------------------------------
    # Compatibility aliases
    # -------------------------------------------------

    IDLE = RuntimeStatus.IDLE

    RUNNING = RuntimeStatus.RUNNING

    FAILED = RuntimeStatus.FAILED


    # =================================================
    # Lifecycle
    # =================================================


    def mark_initializing(self):

        self.status = RuntimeStatus.INITIALIZING



    def mark_started(self):
        """
        Marks runtime as running.
        """

        self.status = RuntimeStatus.RUNNING

        self.started_at = datetime.now(
            timezone.utc
        )



    def mark_stopping(self):

        self.status = RuntimeStatus.STOPPING



    def mark_stopped(self):
        """
        Marks runtime as stopped.
        """

        self.status = RuntimeStatus.IDLE

        self.stopped_at = datetime.now(
            timezone.utc
        )



    # =================================================
    # Cycles
    # =================================================


    def update_cycle(
        self,
        cycle: int,
    ):
        """
        Updates cognitive cycle counter.
        """

        self.cycles = cycle



    # =================================================
    # Errors
    # =================================================


    def register_error(
        self,
        error: str,
    ):
        """
        Registers runtime failure.
        """

        self.status = RuntimeStatus.FAILED

        self.errors.append(
            error
        )



    # =================================================
    # Services
    # =================================================


    def register_service(
        self,
        name: str,
        status: str = "registered",
    ):
        """
        Registers a runtime service.
        """

        self.services[name] = status



    def update_service(
        self,
        name: str,
        status: str,
    ):
        """
        Updates service lifecycle status.
        """

        self.services[name] = status



    def remove_service(
        self,
        name: str,
    ):
        """
        Removes a service.
        """

        self.services.pop(
            name,
            None
        )



    # =================================================
    # Serialization
    # =================================================


    def to_dict(self) -> dict:
        """
        Exports runtime state.
        """

        return {

            "status": self.status.value,

            "created_at": (
                self.created_at.isoformat()
                if self.created_at
                else None
            ),

            "started_at": (
                self.started_at.isoformat()
                if self.started_at
                else None
            ),

            "stopped_at": (
                self.stopped_at.isoformat()
                if self.stopped_at
                else None
            ),

            "cycles": self.cycles,

            "errors": list(
                self.errors
            ),

            "services": dict(
                self.services
            ),
        }



    def from_dict(
        self,
        data: dict,
    ):
        """
        Restores runtime state.
        """

        if "status" in data:

            self.status = RuntimeStatus(
                data["status"]
            )


        self.cycles = data.get(
            "cycles",
            0
        )


        self.errors = list(
            data.get(
                "errors",
                []
            )
        )


        self.services = dict(
            data.get(
                "services",
                {}
            )
        )



    # =================================================
    # Reset
    # =================================================


    def reset(self):
        """
        Reset runtime statistics.
        """

        self.status = RuntimeStatus.IDLE

        self.started_at = None

        self.stopped_at = None

        self.cycles = 0

        self.errors.clear()

        self.services.clear()