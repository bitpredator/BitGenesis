from __future__ import annotations

import pytest

from bitgenesis.kernel.exceptions import ServiceNotFoundError
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.service_manager import ServiceManager


class AlphaService(KernelService):

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass


class BetaService(KernelService):

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass


def test_get_returns_registered_service():

    manager = ServiceManager()

    service = AlphaService()

    manager.register(
        service,
    )

    assert (
        manager.get(
            AlphaService,
        )
        is service
    )


def test_contains_registered_service():

    manager = ServiceManager()

    manager.register(
        AlphaService(),
    )

    assert manager.contains(
        AlphaService,
    )


def test_contains_unknown_service():

    manager = ServiceManager()

    assert not manager.contains(
        AlphaService,
    )


def test_require_returns_registered_service():

    manager = ServiceManager()

    service = AlphaService()

    manager.register(
        service,
    )

    assert (
        manager.require(
            AlphaService,
        )
        is service
    )


def test_require_unknown_service_raises():

    manager = ServiceManager()

    with pytest.raises(
        ServiceNotFoundError,
    ):

        manager.require(
            AlphaService,
        )


def test_discover_returns_all_services():

    manager = ServiceManager()

    alpha = AlphaService()

    beta = BetaService()

    manager.register(
        alpha,
    )

    manager.register(
        beta,
    )

    services = manager.discover()

    assert len(
        services,
    ) == 2

    assert alpha in services

    assert beta in services


def test_discover_empty_registry():

    manager = ServiceManager()

    assert manager.discover() == ()