from bitgenesis.runtime.service_registry import (
    ServiceRegistry,
)



class DummyService:
    pass



def test_service_registry_register():

    registry = ServiceRegistry()


    service = DummyService()


    descriptor = registry.register(
        service
    )


    assert descriptor.service is service

    assert descriptor.name == (
        "DummyService"
    )



def test_service_registry_discover():

    registry = ServiceRegistry()


    service = DummyService()


    registry.register(
        service,
        name="dummy",
    )


    result = registry.discover(
        "dummy"
    )


    assert result is not None

    assert result.service is service



def test_service_registry_unregister():

    registry = ServiceRegistry()


    registry.register(
        DummyService(),
        name="dummy",
    )


    removed = registry.unregister(
        "dummy"
    )


    assert removed is True

    assert registry.exists(
        "dummy"
    ) is False



def test_service_registry_metadata_search():

    registry = ServiceRegistry()


    registry.register(
        DummyService(),
        name="memory",
        metadata={
            "category": "storage",
        },
    )


    registry.register(
        DummyService(),
        name="planner",
        metadata={
            "category": "cognition",
        },
    )


    result = registry.find_by_metadata(
        "category",
        "storage",
    )


    assert len(result) == 1

    assert result[0].name == "memory"



def test_service_registry_all():

    registry = ServiceRegistry()


    registry.register(
        DummyService(),
        name="one",
    )


    registry.register(
        DummyService(),
        name="two",
    )


    services = registry.all()


    assert len(services) == 2



def test_service_registry_len():

    registry = ServiceRegistry()


    registry.register(
        DummyService()
    )


    assert len(registry) == 1