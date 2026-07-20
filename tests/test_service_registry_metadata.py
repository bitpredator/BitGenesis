from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.service import KernelService


class DemoService(KernelService):

    name = "memory"

    version = "2.0.0"


def test_registry_can_find_by_name():

    registry = ServiceRegistry()

    service = DemoService()

    registry.register(service)

    assert registry.get_by_name("memory") is service


def test_service_metadata():

    service = DemoService()

    metadata = service.metadata()

    assert metadata["name"] == "memory"

    assert metadata["version"] == "2.0.0"

    assert metadata["enabled"] is True