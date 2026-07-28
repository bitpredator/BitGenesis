from __future__ import annotations

from dataclasses import dataclass

from bitgenesis.runtime.runtime_metrics import RuntimeMetrics


@dataclass(slots=True)
class RuntimeStatistics:
    """
    High-level runtime statistics.

    Provides a stable read-only view over RuntimeMetrics.
    """

    metrics: RuntimeMetrics

    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    @property
    def total_ticks(self) -> int:

        return self.metrics.ticks

    @property
    def total_executions(self) -> int:

        return self.metrics.executions

    @property
    def successful_executions(self) -> int:

        return self.metrics.successful_executions

    @property
    def failed_executions(self) -> int:

        return self.metrics.failed_executions

    @property
    def execution_success_rate(self) -> float:

        return self.metrics.execution_success_rate

    @property
    def average_execution_time_ms(self) -> float:

        return self.metrics.average_execution_time_ms

    # --------------------------------------------------
    # Services
    # --------------------------------------------------

    @property
    def services_executed(self) -> int:

        return self.metrics.services_executed

    @property
    def failed_services(self) -> int:

        return self.metrics.failed_services

    @property
    def average_service_time_ms(self) -> float:

        return self.metrics.average_service_time_ms

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "ticks": self.total_ticks,
            "executions": self.total_executions,
            "successful_executions": self.successful_executions,
            "failed_executions": self.failed_executions,
            "execution_success_rate": self.execution_success_rate,
            "average_execution_time_ms": self.average_execution_time_ms,
            "services_executed": self.services_executed,
            "failed_services": self.failed_services,
            "average_service_time_ms": self.average_service_time_ms,
        }