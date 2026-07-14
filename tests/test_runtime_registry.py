from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.action import RuntimeAction
from bitgenesis.runtime.result import ActionResult


class DummyAction(RuntimeAction):

    name = "dummy"


    def execute(self, context):

        return ActionResult.ok(
            "done"
        )



def test_register_action():

    registry = ActionRegistry()

    registry.register(
        "dummy",
        DummyAction,
    )

    assert registry.get("dummy") == DummyAction



def test_create_action():

    registry = ActionRegistry()

    registry.register(
        "dummy",
        DummyAction,
    )

    action = registry.create(
        "dummy"
    )

    assert isinstance(
        action,
        DummyAction,
    )



def test_unknown_action():

    registry = ActionRegistry()

    assert registry.create(
        "missing"
    ) is None