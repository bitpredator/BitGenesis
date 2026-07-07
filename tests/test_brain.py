from bitgenesis.core.brain import Brain
from bitgenesis.core.lifecycle import BrainState
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)


def create_event():

    return Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        payload={
            "message": "Brain initialized"
        },
        priority=EventPriority.NORMAL,
    )


def test_brain_can_be_created():

    brain = Brain()

    assert brain is not None


def test_brain_starts_idle():

    brain = Brain()

    assert brain.state == BrainState.IDLE


def test_brain_can_answer_identity_question():

    brain = Brain()

    response = brain.ask(
        "Who created you?"
    )

    assert response == "My creator is Bitpredator."


def test_brain_observe_stores_memory():

    brain = Brain()

    event = create_event()

    memory = brain.observe(event)

    memories = brain.remember()

    assert memory in memories
    assert len(memories) == 1


def test_brain_returns_to_idle_after_observe():

    brain = Brain()

    brain.observe(create_event())

    assert brain.state == BrainState.IDLE


def test_brain_returns_to_idle_after_question():

    brain = Brain()

    brain.ask("Who are you?")

    assert brain.state == BrainState.IDLE


def test_brain_can_run_inference():

    brain = Brain()

    facts = [
        "Python is_a ProgrammingLanguage",
        "User likes Python",
    ]

    inferred = brain.infer(facts)

    assert inferred == [
        "User likes ProgrammingLanguage"
    ]


def test_brain_returns_to_idle_after_inference():

    brain = Brain()

    brain.infer([])

    assert brain.state == BrainState.IDLE


def test_brain_can_run_reflection():

    brain = Brain()

    facts = [
        "Python",
        "Rust",
        "C++",
    ]

    reflections = brain.reflect(facts)

    assert reflections == [
        "The user enjoys programming languages."
    ]


def test_brain_returns_to_idle_after_reflection():

    brain = Brain()

    brain.reflect([])

    assert brain.state == BrainState.IDLE


def test_brain_remember_initially_empty():

    brain = Brain()

    assert list(brain.remember()) == []


def test_brain_knowledge_initially_empty():

    brain = Brain()

    assert list(brain.knowledge()) == []

def test_brain_version():

    brain = Brain()

    assert brain.version == "0.1.0"


def test_brain_initial_stats():

    brain = Brain()

    stats = brain.stats()

    assert stats.version == "0.1.0"
    assert stats.state == "idle"


def test_brain_stats_memory_count():

    brain = Brain()

    stats = brain.stats()

    assert stats.memories == 0


def test_brain_stats_knowledge_count():

    brain = Brain()

    stats = brain.stats()

    assert stats.knowledge == 0    