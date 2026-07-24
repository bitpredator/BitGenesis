from bitgenesis.kernel.dependency_resolver import DependencyResolver
from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.service import KernelService



class DatabaseService(
    KernelService
):
    pass



class BrainService(
    KernelService
):
    pass



class RuntimeService(
    KernelService
):
    pass




def test_dependency_resolver_orders_dependencies():

    manager = ServiceManager()


    database = DatabaseService()
    brain = BrainService()
    runtime = RuntimeService()


    manager.register(database)
    manager.register(brain)
    manager.register(runtime)


    resolver = DependencyResolver(
        manager
    )


    resolver.add_dependency(
        BrainService,
        DatabaseService,
    )


    resolver.add_dependency(
        RuntimeService,
        BrainService,
    )


    result = resolver.resolve(
        RuntimeService
    )


    assert result == [
        database,
        brain,
        runtime,
    ]




def test_dependency_resolver_without_dependencies():

    manager = ServiceManager()


    service = RuntimeService()


    manager.register(
        service
    )


    resolver = DependencyResolver(
        manager
    )


    result = resolver.resolve(
        RuntimeService
    )


    assert result == [
        service
    ]




def test_dependency_resolver_missing_service():

    manager = ServiceManager()


    resolver = DependencyResolver(
        manager
    )


    try:

        resolver.resolve(
            RuntimeService
        )

        assert False

    except Exception:

        assert True