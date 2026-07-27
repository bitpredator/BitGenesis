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

from bitgenesis.runtime.service_registry import (
    ServiceRegistry,
)



class ServiceOrchestrator:
    """
    Coordinates execution of runtime services.

    Responsibilities:

    - register services
    - unregister services
    - execute ordered services
    - manage lifecycle
    - collect execution results
    - isolate failures

    Compatibility:
    - supports ServiceRegistry
    - supports legacy services list
    """



    def __init__(
        self,
        registry: ServiceRegistry | None = None,
        services: list[object] | None = None,
    ):


        #
        # Compatibility:
        #
        # Old usage:
        #
        # ServiceOrchestrator([service])
        #
        # New usage:
        #
        # ServiceOrchestrator(
        #     registry=ServiceRegistry()
        # )
        #

        if isinstance(
            registry,
            list,
        ):

            services = registry

            registry = None



        self.registry = (
            registry
            or ServiceRegistry()
        )



        if services:

            for service in services:

                self.register(
                    service
                )



    # --------------------------------------------------
    # Compatibility helpers
    # --------------------------------------------------

    def _services(self):

        #
        # Extra protection in case
        # external code injects a list
        #

        if isinstance(
            self.registry,
            list,
        ):

            return [
                type(
                    "ServiceDescriptor",
                    (),
                    {
                        "service": service,
                        "name": type(service).__name__,
                    },
                )
                for service in self.registry
            ]



        return self.registry.all()



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        service: object,
        name: str | None = None,
        metadata: dict | None = None,
    ):

        return self.registry.register(
            service,
            name=name,
            metadata=metadata,
        )



    def unregister(
        self,
        name: str,
    ):

        return self.registry.unregister(
            name
        )



    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------

    def discover(
        self,
        name: str,
    ):

        return self.registry.discover(
            name
        )



    def all(self):

        return self._services()



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start_services(
        self,
        context: ServiceContext,
    ):


        for descriptor in self._services():

            service = descriptor.service


            start = getattr(
                service,
                "start",
                None,
            )


            if start:

                start(
                    context
                )



    def stop_services(
        self,
        context: ServiceContext,
    ):


        for descriptor in self._services():

            service = descriptor.service


            stop = getattr(
                service,
                "stop",
                None,
            )


            if stop:

                stop(
                    context
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



        for descriptor in self._services():

            execution = self._execute_service(
                descriptor.service,
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

            services_executed=len(
                executions
            ),

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