from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class RuntimeState:
    """
    Persistent state container for CognitiveRuntime.

    Stores runtime execution information that survives
    across cognitive cycles during the lifetime of the runtime.

    This is intentionally separated from CognitiveState,
    which represents only the temporary cognitive pipeline state.
    """

    # --------------------------------------------------
    # Execution statistics
    # --------------------------------------------------

    cycle_count: int = 0

    successful_cycles: int = 0

    failed_cycles: int = 0


    # --------------------------------------------------
    # Current execution information
    # --------------------------------------------------

    is_running: bool = False

    current_cycle_id: str | None = None

    last_cycle_id: str | None = None


    # --------------------------------------------------
    # Context tracking
    # --------------------------------------------------

    last_context_id: str | None = None

    last_input: Any | None = None


    # --------------------------------------------------
    # Timing information
    # --------------------------------------------------

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    last_started_at: datetime | None = None

    last_completed_at: datetime | None = None


    # --------------------------------------------------
    # Error tracking
    # --------------------------------------------------

    last_error: str | None = None


    # --------------------------------------------------
    # Runtime operations
    # --------------------------------------------------

    def start_cycle(
        self,
        cycle_id: str | None = None,
    ) -> None:
        """
        Marks the beginning of a cognitive cycle.
        """

        self.is_running = True

        self.current_cycle_id = cycle_id

        self.last_started_at = datetime.utcnow()

        self.last_error = None


    def complete_cycle(
        self,
        context_id: str | None = None,
    ) -> None:
        """
        Marks a successful cognitive cycle.
        """

        self.is_running = False

        self.cycle_count += 1

        self.successful_cycles += 1

        self.last_cycle_id = (
            self.current_cycle_id
        )

        self.last_context_id = context_id

        self.last_completed_at = datetime.utcnow()

        self.current_cycle_id = None


    def fail_cycle(
        self,
        error: Exception | str,
    ) -> None:
        """
        Marks a failed cognitive cycle.
        """

        self.is_running = False

        self.cycle_count += 1

        self.failed_cycles += 1

        self.last_error = str(error)

        self.last_completed_at = datetime.utcnow()

        self.current_cycle_id = None


    def reset(self) -> None:
        """
        Clears runtime statistics.
        """

        self.cycle_count = 0

        self.successful_cycles = 0

        self.failed_cycles = 0

        self.current_cycle_id = None

        self.last_cycle_id = None

        self.last_context_id = None

        self.last_input = None

        self.last_error = None

        self.is_running = False