from bitgenesis.core.config import BrainConfig
from bitgenesis.core.lifecycle import BrainState
from bitgenesis.core.stats import BrainStats
from bitgenesis.core.version import VERSION

from bitgenesis.cognition import CognitiveManager

from bitgenesis.dialogue.response_engine import ResponseEngine

from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.factory import MemoryFactory

from bitgenesis.knowledge.registry import KnowledgeRegistry
from bitgenesis.knowledge.inference_engine import InferenceEngine

from bitgenesis.reasoning.reflection_engine import ReflectionEngine


class Brain:

    def __init__(self, config=None):

        self.config = config or BrainConfig()

        self.state = BrainState.IDLE

        # -------------------------------------------------
        # Core cognitive subsystems
        # -------------------------------------------------

        self.memory_store = MemoryStore()

        self.knowledge_registry = KnowledgeRegistry()

        self.memory_factory = MemoryFactory()

        self.inference_engine = InferenceEngine()

        self.reflection_engine = ReflectionEngine()

        self.response_engine = ResponseEngine(
            memory_store=self.memory_store,
        )

        # -------------------------------------------------
        # Cognitive runtime
        # -------------------------------------------------

        self.cognitive_manager = CognitiveManager(
            memory_store=self.memory_store,
            knowledge_registry=self.knowledge_registry,
            inference_engine=self.inference_engine,
            reflection_engine=self.reflection_engine,
            response_engine=self.response_engine,
            memory_factory=self.memory_factory,
        )

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    @property
    def version(self):

        return str(VERSION)


    @property
    def cognitive_context(self):

        return self.cognitive_manager.last_context


    def stats(self):

        return BrainStats(
            memories=len(self.memory_store.all()),
            episodes=0,
            knowledge=len(self.knowledge_registry.all()),
            state=self.state.value,
            version=self.version,
        )


    # -------------------------------------------------
    # Cognition
    # -------------------------------------------------

    def think(self, input_data=None):

        """
        Executes a complete cognitive cycle.

        This is the primary entry point for the
        cognitive architecture.
        """

        self.state = BrainState.THINKING

        try:

            return self.cognitive_manager.execute(
                input_data
            )

        finally:

            self.state = BrainState.IDLE


    # -------------------------------------------------
    # Dialogue
    # -------------------------------------------------

    def ask(self, question: str):

        self.state = BrainState.RESPONDING

        try:

            return self.response_engine.respond(question)

        finally:

            self.state = BrainState.IDLE


    # -------------------------------------------------
    # Observation
    # -------------------------------------------------

    def observe(self, event):

        self.state = BrainState.OBSERVING

        try:

            memory = self.memory_factory.from_event(event)

            self.memory_store.add(memory)

            return memory

        finally:

            self.state = BrainState.IDLE


    # -------------------------------------------------
    # Inference
    # -------------------------------------------------

    def infer(self, facts):

        self.state = BrainState.INFERRING

        try:

            return self.inference_engine.infer(facts)

        finally:

            self.state = BrainState.IDLE


    # -------------------------------------------------
    # Reflection
    # -------------------------------------------------

    def reflect(self, facts):

        self.state = BrainState.REFLECTING

        try:

            return self.reflection_engine.reflect(facts)

        finally:

            self.state = BrainState.IDLE


    # -------------------------------------------------
    # Memory
    # -------------------------------------------------

    def remember(self):

        return self.memory_store.all()


    # -------------------------------------------------
    # Knowledge
    # -------------------------------------------------

    def knowledge(self):

        return self.knowledge_registry.all()