from bitgenesis.runtime.runtime_manager import RuntimeManager


def test_runtime_manager_starts():

    manager = RuntimeManager()

    manager.start()

    assert manager.running is True



def test_runtime_manager_stops():

    manager = RuntimeManager()

    manager.start()

    manager.stop()

    assert manager.running is False