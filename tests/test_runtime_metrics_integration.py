from __future__ import annotations


from bitgenesis.runtime.runtime_manager import (
    RuntimeManager,
)


class DummyService:

    def __init__(self):

        self.executed = False


    def tick(self):

        self.executed = True



def test_runtime_manager_initializes_metrics():

    runtime = RuntimeManager()


    assert runtime.metrics is not None

    assert runtime.statistics is not None



def test_runtime_manager_tick_updates_metrics():

    service = DummyService()


    runtime = RuntimeManager(
        services=[
            service
        ]
    )


    runtime.start()


    runtime.tick()


    assert runtime.metrics.ticks == 1



def test_runtime_manager_snapshot():

    runtime = RuntimeManager()


    snapshot = runtime.snapshot()


    assert snapshot is not None

    assert snapshot.statistics is not None

    assert (
        snapshot.statistics.total_ticks
        == 0
    )



def test_runtime_manager_service_metrics():

    service = DummyService()


    runtime = RuntimeManager(
        services=[
            service
        ]
    )


    runtime.start()


    runtime.tick()


    assert (
        runtime.metrics.services_executed
        >= 1
    )


    assert service.executed is True



def test_runtime_manager_statistics_export():

    runtime = RuntimeManager()


    data = runtime.statistics.to_dict()


    assert "ticks" in data

    assert "executions" in data

    assert "services_executed" in data