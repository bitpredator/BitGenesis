from bitgenesis.kernel.container import DependencyContainer



class Database:

    pass



class Repository:


    def __init__(
        self,
        database: Database,
    ):

        self.database = database



def test_dependency_auto_resolution():

    container = DependencyContainer()


    repository = container.resolve(
        Repository
    )


    assert repository is not None

    assert isinstance(
        repository.database,
        Database,
    )



def test_singleton_resolution():

    container = DependencyContainer()


    first = container.resolve(
        Database
    )

    second = container.resolve(
        Database
    )


    assert first is second