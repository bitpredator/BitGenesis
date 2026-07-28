from bitgenesis.runtime.runtime_metrics import RuntimeMetrics
from bitgenesis.runtime.runtime_statistics import RuntimeStatistics


def test_runtime_statistics_reads_metrics():

    metrics = RuntimeMetrics()

    metrics.record_tick()
    metrics.record_execution(True, 15)
    metrics.record_services(
        executed=2,
        failed=0,
        duration_ms=30,
    )

    stats = RuntimeStatistics(metrics)

    assert stats.total_ticks == 1
    assert stats.total_executions == 1
    assert stats.successful_executions == 1
    assert stats.failed_executions == 0
    assert stats.services_executed == 2


def test_runtime_statistics_to_dict():

    metrics = RuntimeMetrics()

    metrics.record_execution(True, 12)

    stats = RuntimeStatistics(metrics)

    data = stats.to_dict()

    assert data["executions"] == 1
    assert data["successful_executions"] == 1
    assert data["failed_executions"] == 0
    assert "execution_success_rate" in data