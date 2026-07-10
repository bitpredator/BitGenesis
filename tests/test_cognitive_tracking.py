from bitgenesis.core.brain import Brain


def test_cognitive_cycle_tracking():

    brain = Brain()

    context = brain.think(
        "hello"
    )

    assert context.cycle_id

    assert len(
        context.stage_history
    ) == 8

    for stage in context.stage_history:
        assert stage["success"] is True