from bitgenesis.kernel.bootstrap import bootstrap
from bitgenesis.runtime.service import RuntimeService


def test_bootstrap_registers_runtime_service():

    bus, kernel, store = bootstrap()

    service = kernel.get_service(
        RuntimeService
    )

    assert service is not None

    assert service.running is True