from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeMetrics:
    """
    Runtime execution counters.

    This object collects low-level runtime metrics.
    """

    ticks: int = 0

    executions: int = 0

    successful_executions: int = 0

    failed_executions: int = 0

    services_executed: int = 0

    failed_services: int = 0

    total_execution_time_ms: float = 0.0

    total_service_time_ms: float = 0.0

    # --------------------------------------------------
    # Recording
    # --------------------------------------------------

    def record_tick(self):

        self.ticks += 1

    def record_execution(
        self,
        success: bool,
        duration_ms: float,
    ):

        self.executions += 1

        self.total_execution_time_ms += duration_ms

        if success:
            self.successful_executions += 1
        else:
            self.failed_executions += 1

    def record_services(
        self,
        executed: int,
        failed: int,
        duration_ms: float = 0.0,
    ):

        self.services_executed += executed

        self.failed_services += failed

        self.total_service_time_ms += duration_ms

    # --------------------------------------------------
    # Derived metrics
    # --------------------------------------------------

    @property
    def execution_success_rate(self) -> float:

        if self.executions == 0:
            return 0.0

        return (
            self.successful_executions
            / self.executions
        )

    @property
    def average_execution_time_ms(self) -> float:

        if self.executions == 0:
            return 0.0

        return (
            self.total_execution_time_ms
            / self.executions
        )

    @property
    def average_service_time_ms(self) -> float:

        if self.services_executed == 0:
            return 0.0

        return (
            self.total_service_time_ms
            / self.services_executed
        )