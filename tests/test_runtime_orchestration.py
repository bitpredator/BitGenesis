from __future__ import annotations

from bitgenesis.runtime.service_context import ServiceContext
from bitgenesis.runtime.service_orchestrator import ServiceOrchestrator



class RuntimeService:

    def __init__(self):
        self.called = False


    def execute(
        self,
        context,
    ):

        self.called = True

        context.with_metadata(
            "service",
            "runtime_service",
        )


        return True



class LegacyRuntimeService:

    def __init__(self):
        self.called = False


    def tick(self):

        self.called = True

        return "tick"



def test_runtime_orchestration_executes_runtime_services():

    service = RuntimeService()


    orchestrator = ServiceOrchestrator(
        [
            service
        ]
    )


    context = ServiceContext()


    result = orchestrator.execute(
        context
    )


    assert result.success

    assert result.services_executed == 1

    assert service.called



def test_runtime_orchestration_passes_context():

    service = RuntimeService()


    context = ServiceContext()


    orchestrator = ServiceOrchestrator(
        [
            service
        ]
    )


    orchestrator.execute(
        context
    )


    assert (
        context.metadata["service"]
        ==
        "runtime_service"
    )



def test_runtime_orchestration_supports_tick_services():

    service = LegacyRuntimeService()


    orchestrator = ServiceOrchestrator(
        [
            service
        ]
    )


    result = orchestrator.execute(
        ServiceContext()
    )


    assert result.success

    assert service.called

    assert result.services_executed == 1