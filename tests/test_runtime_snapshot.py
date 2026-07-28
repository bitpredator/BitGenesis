from datetime import datetime

from bitgenesis.runtime.runtime_metrics import RuntimeMetrics
from bitgenesis.runtime.runtime_statistics import RuntimeStatistics
from bitgenesis.runtime.runtime_snapshot import RuntimeSnapshot


def test_runtime_snapshot_creation():

    metrics = RuntimeMetrics()

    stats = RuntimeStatistics(metrics)

    snapshot = RuntimeSnapshot(
        created_at=datetime.now(),
        statistics=stats,
    )

    assert snapshot.statistics is stats


def test_runtime_snapshot_to_dict():

    metrics = RuntimeMetrics()

    stats = RuntimeStatistics(metrics)

    snapshot = RuntimeSnapshot(
        created_at=datetime.now(),
        statistics=stats,
    )

    data = snapshot.to_dict()

    assert "created_at" in data
    assert "statistics" in data


def test_runtime_snapshot_string_representation():

    metrics = RuntimeMetrics()

    metrics.record_tick()

    stats = RuntimeStatistics(metrics)

    snapshot = RuntimeSnapshot(
        created_at=datetime.now(),
        statistics=stats,
    )

    text = str(snapshot)

    assert "RuntimeSnapshot" in text
    assert "ticks=1" in text