from __future__ import annotations

from datetime import datetime

from bitgenesis.runtime.service_context import ServiceContext
from bitgenesis.runtime.service_execution import ServiceExecution
from bitgenesis.runtime.orchestration_result import OrchestrationResult



class ServiceOrchestrator:
    """
    Coordinates execution of runtime services.

    Responsibilities:

    - execute ordered services
    - provide shared service context
    - collect execution results
    - isolate service failures
    """


    def __init__(
        self,
        services: list[object] | None = None,
    ):

        self.services = (
            services
            or []
        )



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        service: object,
    ):

        if service not in self.services:

            self.services.append(
                service
            )



    def unregister(
        self,
        service: object,
    ):

        if service in self.services:

            self.services.remove(
                service
            )



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def execute(
        self,
        context: ServiceContext,
    ) -> OrchestrationResult:
        """
        Execute all registered services.
        """


        executions: list[ServiceExecution] = []


        for service in self.services:

            execution = self._execute_service(
                service,
                context,
            )

            executions.append(
                execution
            )



        return OrchestrationResult(
            success=all(
                execution.success
                for execution in executions
            ),
            executions=executions,
            services_executed=len(executions),
            failed_services=sum(
                1
                for execution in executions
                if not execution.success
            ),
        )



    # --------------------------------------------------
    # Internal execution
    # --------------------------------------------------

    def _execute_service(
        self,
        service: object,
        context: ServiceContext,
    ) -> ServiceExecution:


        name = type(service).__name__


        started = datetime.now()


        success = True


        metadata = {}



        try:

            execute = getattr(
                service,
                "execute",
                None,
            )


            if execute:

                result = execute(
                    context
                )


                metadata["result"] = result


            else:

                tick = getattr(
                    service,
                    "tick",
                    None,
                )


                if tick:

                    result = tick()

                    metadata["result"] = result



        except Exception as exc:

            success = False

            metadata["error"] = str(exc)



        finished = datetime.now()


        duration = (
            finished - started
        ).total_seconds() * 1000



        return ServiceExecution(
            service_name=name,
            success=success,
            started_at=started,
            finished_at=finished,
            duration_ms=duration,
            metadata=metadata,
        )