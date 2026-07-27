from __future__ import annotations

from datetime import datetime

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.events.event_bus import EventBus


from bitgenesis.runtime.service_context import (
    ServiceContext,
)

from bitgenesis.runtime.service_execution import (
    ServiceExecution,
)

from bitgenesis.runtime.service_state import (
    ServiceState,
)

from bitgenesis.runtime.orchestration_result import (
    OrchestrationResult,
)



class ServiceOrchestrator:
    """
    Coordinates runtime service lifecycle and execution.

    Responsibilities:

    - register services
    - manage service lifecycle
    - execute ordered services
    - provide shared context
    - isolate service failures
    """



    def __init__(
        self,
        services: list[object] | None = None,
        event_bus: EventBus | None = None,
    ):

        self.services = (
            services
            or []
        )

        self.event_bus = event_bus


        self.states = {
            service: ServiceState.CREATED
            for service in self.services
        }



    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type: EventType,
        service,
    ):

        if self.event_bus is None:
            return


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=event_type,
                source="service_orchestrator",
                payload={
                    "service": (
                        type(service).__name__
                    ),
                },
            )
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


            self.states[service] = (
                ServiceState.CREATED
            )


            self._emit(
                EventType.SERVICE_REGISTERED,
                service,
            )



    def unregister(
        self,
        service: object,
    ):

        if service in self.services:

            self.services.remove(
                service
            )


            self.states.pop(
                service,
                None,
            )


            self._emit(
                EventType.SERVICE_UNREGISTERED,
                service,
            )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start_services(
        self,
        context: ServiceContext,
    ):


        for service in self.services:

            try:

                self.states[service] = (
                    ServiceState.STARTING
                )


                self._emit(
                    EventType.SERVICE_STARTING,
                    service,
                )


                start = getattr(
                    service,
                    "start",
                    None,
                )


                if start:

                    start(
                        context
                    )


                self.states[service] = (
                    ServiceState.RUNNING
                )


                self._emit(
                    EventType.SERVICE_STARTED,
                    service,
                )


            except Exception:

                self.states[service] = (
                    ServiceState.FAILED
                )


                self._emit(
                    EventType.SERVICE_FAILED,
                    service,
                )



    def stop_services(
        self,
        context: ServiceContext,
    ):


        for service in self.services:

            try:

                self.states[service] = (
                    ServiceState.STOPPING
                )


                self._emit(
                    EventType.SERVICE_STOPPING,
                    service,
                )


                stop = getattr(
                    service,
                    "stop",
                    None,
                )


                if stop:

                    stop(
                        context
                    )


                self.states[service] = (
                    ServiceState.STOPPED
                )


                self._emit(
                    EventType.SERVICE_STOPPED,
                    service,
                )


            except Exception:

                self.states[service] = (
                    ServiceState.FAILED
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
            state=(
                ServiceState.RUNNING
                if success
                else ServiceState.FAILED
            ),
            started_at=started,
            finished_at=finished,
            duration_ms=duration,
            metadata=metadata,
        )