from bitgenesis.runtime.runtime_metrics import RuntimeMetrics


def test_runtime_metrics_defaults():

    metrics = RuntimeMetrics()

    assert metrics.ticks == 0
    assert metrics.executions == 0
    assert metrics.successful_executions == 0
    assert metrics.failed_executions == 0
    assert metrics.services_executed == 0
    assert metrics.failed_services == 0
    assert metrics.total_execution_time_ms == 0.0
    assert metrics.total_service_time_ms == 0.0


def test_runtime_metrics_record_tick():

    metrics = RuntimeMetrics()

    metrics.record_tick()
    metrics.record_tick()

    assert metrics.ticks == 2


def test_runtime_metrics_record_successful_execution():

    metrics = RuntimeMetrics()

    metrics.record_execution(
        success=True,
        duration_ms=10,
    )

    assert metrics.executions == 1
    assert metrics.successful_executions == 1
    assert metrics.failed_executions == 0
    assert metrics.total_execution_time_ms == 10


def test_runtime_metrics_record_failed_execution():

    metrics = RuntimeMetrics()

    metrics.record_execution(
        success=False,
        duration_ms=25,
    )

    assert metrics.executions == 1
    assert metrics.successful_executions == 0
    assert metrics.failed_executions == 1
    assert metrics.total_execution_time_ms == 25


def test_runtime_metrics_record_services():

    metrics = RuntimeMetrics()

    metrics.record_services(
        executed=5,
        failed=2,
        duration_ms=50,
    )

    assert metrics.services_executed == 5
    assert metrics.failed_services == 2
    assert metrics.total_service_time_ms == 50


def test_runtime_metrics_success_rate():

    metrics = RuntimeMetrics()

    metrics.record_execution(True, 10)
    metrics.record_execution(True, 20)
    metrics.record_execution(False, 30)

    assert metrics.execution_success_rate == 2 / 3


def test_runtime_metrics_average_execution_time():

    metrics = RuntimeMetrics()

    metrics.record_execution(True, 10)
    metrics.record_execution(True, 20)

    assert metrics.average_execution_time_ms == 15


def test_runtime_metrics_average_service_time():

    metrics = RuntimeMetrics()

    metrics.record_services(
        executed=2,
        failed=0,
        duration_ms=40,
    )

    assert metrics.average_service_time_ms == 20