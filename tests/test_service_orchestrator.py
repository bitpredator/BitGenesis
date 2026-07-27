from __future__ import annotations

from bitgenesis.runtime.service_context import ServiceContext
from bitgenesis.runtime.service_orchestrator import ServiceOrchestrator



class DummyService:

    def __init__(self):
        self.executed = False


    def execute(
        self,
        context,
    ):

        self.executed = True

        return {
            "status": "ok"
        }



class FailingService:

    def execute(
        self,
        context,
    ):

        raise RuntimeError(
            "service failure"
        )



def test_service_orchestrator_executes_service():

    service = DummyService()


    orchestrator = ServiceOrchestrator(
        services=[
            service
        ]
    )


    result = orchestrator.execute(
        ServiceContext()
    )


    assert result.success

    assert result.services_executed == 1

    assert service.executed



def test_service_orchestrator_collects_metadata():

    service = DummyService()


    orchestrator = ServiceOrchestrator(
        services=[
            service
        ]
    )


    result = orchestrator.execute(
        ServiceContext()
    )


    execution = result.executions[0]


    assert execution.success

    assert (
        execution.metadata["result"]
        ==
        {
            "status": "ok"
        }
    )



def test_service_orchestrator_handles_failure():

    orchestrator = ServiceOrchestrator(
        services=[
            FailingService()
        ]
    )


    result = orchestrator.execute(
        ServiceContext()
    )


    assert not result.success

    assert result.failed_services == 1

    assert (
        result.executions[0].metadata["error"]
        ==
        "service failure"
    )