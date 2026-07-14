from dataclasses import dataclass

from bitgenesis.kernel.bootstrap import bootstrap
from bitgenesis.runtime.service import RuntimeService


@dataclass
class DummyStep:
    """
    Minimal execution step used for runtime integration tests.
    """

    action: str
    target: str



def create_plan(step):
    """
    Creates a minimal execution plan compatible
    with Runtime Executor.
    """

    return type(
        "Plan",
        (),
        {
            "steps": [step],
        },
    )()



# --------------------------------------------------
# Bootstrap integration
# --------------------------------------------------


def test_runtime_service_available_after_bootstrap():

    bus, kernel, store = bootstrap()


    runtime = kernel.get_service(
        RuntimeService
    )


    assert runtime is not None

    assert runtime.running is True



# --------------------------------------------------
# Registry integration
# --------------------------------------------------


def test_runtime_registry_available():

    bus, kernel, store = bootstrap()


    runtime = kernel.get_service(
        RuntimeService
    )


    assert runtime.registry is not None

    assert runtime.manager is not None

    assert runtime.manager.executor is not None



# --------------------------------------------------
# Action execution
# --------------------------------------------------


def test_runtime_executes_registered_action():

    bus, kernel, store = bootstrap()


    runtime = kernel.get_service(
        RuntimeService
    )


    step = DummyStep(
        action="store_memory",
        target="BitGenesis runtime integration test",
    )


    plan = create_plan(step)


    result = runtime.manager.executor.execute(
        plan
    )


    assert result.success is True

    assert len(result.results) == 1



# --------------------------------------------------
# Memory action integration
# --------------------------------------------------


def test_runtime_memory_action():

    bus, kernel, store = bootstrap()


    runtime = kernel.get_service(
        RuntimeService
    )


    step = DummyStep(
        action="store_memory",
        target="runtime-memory-test",
    )


    plan = create_plan(step)


    result = runtime.manager.executor.execute(
        plan
    )


    assert result.success is True

    action_result = result.results[0]


    assert action_result.success is True
    assert action_result.data["content"] == "runtime-memory-test"

    assert action_result["action"] == "store_memory"