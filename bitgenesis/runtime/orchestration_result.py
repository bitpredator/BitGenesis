from __future__ import annotations

from dataclasses import dataclass, field

from bitgenesis.runtime.service_execution import ServiceExecution


@dataclass(slots=True)
class OrchestrationResult:
    """
    Result produced by the runtime service orchestrator.

    Contains the execution status of all coordinated services.
    """


    success: bool = True


    executions: list[ServiceExecution] = field(
        default_factory=list
    )


    services_executed: int = 0


    failed_services: int = 0



    @property
    def successful_services(self) -> int:
        """
        Number of successfully executed services.
        """

        return sum(
            1
            for execution in self.executions
            if execution.success
        )



    @property
    def completed(self) -> bool:
        """
        Returns True when at least one service execution exists.
        """

        return bool(
            self.executions
        )



    @property
    def failed(self) -> bool:
        """
        Returns True when orchestration failed.
        """

        return not self.success