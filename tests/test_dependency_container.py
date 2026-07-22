from __future__ import annotations

import pytest

from bitgenesis.kernel.container import DependencyContainer
from bitgenesis.kernel.exceptions import ServiceNotFoundError
from bitgenesis.kernel.service import KernelService


class ExampleService(KernelService):

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass


class AnotherService(KernelService):

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass


def test_container_register_and_get():

    container = DependencyContainer()

    service = ExampleService()

    container.register(service)

    assert container.get(ExampleService) is service


def test_container_require():

    container = DependencyContainer()

    service = ExampleService()

    container.register(service)

    assert container.require(ExampleService) is service


def test_container_require_missing_service():

    container = DependencyContainer()

    with pytest.raises(ServiceNotFoundError):

        container.require(ExampleService)


def test_container_unregister():

    container = DependencyContainer()

    service = ExampleService()

    container.register(service)

    container.unregister(service)

    assert container.get(ExampleService) is None


def test_container_contains():

    container = DependencyContainer()

    service = ExampleService()

    assert not container.contains(ExampleService)

    container.register(service)

    assert container.contains(ExampleService)


def test_container_get_by_name():

    container = DependencyContainer()

    service = ExampleService()

    container.register(service)

    assert (
        container.get_by_name("ExampleService")
        is service
    )


def test_container_discover():

    container = DependencyContainer()

    first = ExampleService()

    second = AnotherService()

    container.register(first)

    container.register(second)

    discovered = container.discover()

    assert len(discovered) == 2

    assert first in discovered

    assert second in discovered


def test_container_clear():

    container = DependencyContainer()

    container.register(
        ExampleService()
    )

    container.register(
        AnotherService()
    )

    container.clear()

    assert container.discover() == ()


def test_container_all_alias():

    container = DependencyContainer()

    service = ExampleService()

    container.register(service)

    assert container.all() == (
        service,
    )


def test_container_registry_property():

    container = DependencyContainer()

    assert container.registry is not None