from __future__ import annotations

from datetime import datetime

from bitgenesis.runtime.service_context import (
    ServiceContext,
)

from bitgenesis.runtime.service_execution import (
    ServiceExecution,
)

from bitgenesis.runtime.orchestration_result import (
    OrchestrationResult,
)



class ServiceOrchestrator:
    """
    Coordinates execution of runtime services.

    Responsibilities:

    - register services
    - unregister services
    - discover services
    - execute ordered services
    - provide shared context
    - collect execution results
    - isolate service failures
    """



    def __init__(
        self,
        services: list[object] | None = None,
        registry=None,
    ):

        self.services = (
            services
            or []
        )

        self.registry = registry



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        service: object,
        name: str | None = None,
        metadata: dict | None = None,
    ):
        """
        Register a runtime service.
        """

        if service not in self.services:

            self.services.append(
                service
            )


        return service



    def unregister(
        self,
        service,
    ):
        """
        Remove a runtime service.
        """

        if service in self.services:

            self.services.remove(
                service
            )

            return True


        if isinstance(service, str):

            found = self.discover(
                service
            )

            if found:

                self.services.remove(
                    found
                )

                return True


        return False



    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------

    def discover(
        self,
        name: str,
    ):
        """
        Discover service by name.
        """

        for service in self.all():

            service_name = (
                getattr(
                    service,
                    "name",
                    None,
                )
                or type(service).__name__
            )


            if service_name == name:

                return service


        return None



    def all(
        self,
    ):
        """
        Return registered services.
        """

        if self.registry is not None:

            return self.registry.all()


        return list(
            self.services
        )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start_services(
        self,
        context: ServiceContext,
    ):

        results = []


        for service in self.all():

            start = getattr(
                service,
                "start",
                None,
            )


            if start:

                try:

                    start(
                        context
                    )

                    results.append(
                        True
                    )

                except Exception:

                    results.append(
                        False
                    )


        return all(results) if results else True



    def stop_services(
        self,
        context: ServiceContext,
    ):

        results = []


        for service in self.all():

            stop = getattr(
                service,
                "stop",
                None,
            )


            if stop:

                try:

                    stop(
                        context
                    )

                    results.append(
                        True
                    )

                except Exception:

                    results.append(
                        False
                    )


        return all(results) if results else True



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

        executions = []


        for service in self.all():

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


        name = (
            getattr(
                service,
                "name",
                None,
            )
            or type(service).__name__
        )


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