from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor



class DatabaseService(KernelService):
    pass



class BrainService(KernelService):
    pass



def test_service_manager_uses_dependencies():

    manager = ServiceManager()

    db = DatabaseService()
    brain = BrainService()


    manager.register(
        db
    )


    manager.register(
        brain,
        ServiceDescriptor(
            name="brain",
            dependencies=(
                DatabaseService,
            )
        )
    )


    result = manager.dependency_resolver.resolve(
        BrainService
    )


    assert result == [
        db,
        brain,
    ]