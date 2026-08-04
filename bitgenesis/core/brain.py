from __future__ import annotations

from bitgenesis.core.config import BrainConfig
from bitgenesis.core.lifecycle import BrainState
from bitgenesis.core.stats import BrainStats
from bitgenesis.core.version import VERSION

from bitgenesis.cognition import CognitiveManager

from bitgenesis.dialogue.response_engine import ResponseEngine

from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.memory.storage.json_backend import JsonMemoryBackend
from bitgenesis.memory.storage.in_memory_backend import InMemoryBackend

from bitgenesis.knowledge.registry import KnowledgeRegistry
from bitgenesis.knowledge.inference_engine import InferenceEngine

from bitgenesis.reasoning.reflection_engine import ReflectionEngine

from bitgenesis.learning.engine import LearningEngine
from bitgenesis.learning.strategies import (
    StatisticsLearningStrategy,
)



class Brain:
    """
    Central cognitive container.

    Coordinates:

    - memory
    - knowledge
    - reasoning
    - reflection
    - dialogue
    - learning
    - runtime services
    - event infrastructure
    """


    def __init__(
        self,
        config=None,
        *,
        event_bus=None,
        runtime=None,
        memory_store=None,
        episode_manager=None,
        identity=None,
        knowledge=None,
    ):


        self.config = config or BrainConfig()

        self.state = BrainState.IDLE



        # -------------------------------------------------
        # External services
        # -------------------------------------------------

        self.event_bus = event_bus

        self.runtime = runtime

        self.episode_manager = episode_manager

        self.identity = identity



        # -------------------------------------------------
        # Memory subsystem
        # -------------------------------------------------

        if memory_store is not None:

            self.memory_store = memory_store


        else:

            if self.config.memory_backend == "json":

                backend = JsonMemoryBackend(
                    self.config.memory_path
                )

            else:

                backend = InMemoryBackend()


            self.memory_store = MemoryStore(
                backend=backend
            )



        # -------------------------------------------------
        # Knowledge subsystem
        # -------------------------------------------------

        self.knowledge_registry = (
            knowledge
            if knowledge is not None
            else KnowledgeRegistry()
        )



        self.memory_factory = MemoryFactory()

        self.inference_engine = InferenceEngine()

        self.reflection_engine = ReflectionEngine()



        # -------------------------------------------------
        # Dialogue subsystem
        # -------------------------------------------------

        self.response_engine = ResponseEngine(
            memory_store=self.memory_store,
        )



        # -------------------------------------------------
        # Learning subsystem
        # -------------------------------------------------

        self.learning_strategy = (
            StatisticsLearningStrategy()
        )


        self.learning_engine = LearningEngine(
            strategies=[
                self.learning_strategy
            ]
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

            learning_engine=self.learning_engine,

            event_bus=self.event_bus,
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



    @property
    def bus(self):

        return self.event_bus



    @property
    def runtime_manager(self):

        return self.runtime



    @property
    def episodes(self):

        if self.episode_manager is None:

            return []

        return self.episode_manager.episodes



    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def stats(self):

        return BrainStats(

            memories=len(
                self.memory_store.all()
            ),

            episodes=len(
                self.episodes
            ),

            knowledge=len(
                self.knowledge_registry.all()
            ),

            state=self.state.value,

            version=self.version,
        )



    # -------------------------------------------------
    # Learning statistics
    # -------------------------------------------------

    def learning_stats(self):

        return self.learning_strategy.statistics()



    # -------------------------------------------------
    # Cognition
    # -------------------------------------------------

    def think(
        self,
        input_data=None,
    ):

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

    def ask(
        self,
        question: str,
    ):

        self.state = BrainState.RESPONDING


        try:

            context = self.think(
                question
            )


            return context.response


        finally:

            self.state = BrainState.IDLE



    # -------------------------------------------------
    # Observation
    # -------------------------------------------------

    def observe(
        self,
        event,
    ):

        self.state = BrainState.OBSERVING


        try:

            memory = self.memory_factory.from_event(
                event
            )


            self.memory_store.add(
                memory
            )


            return memory


        finally:

            self.state = BrainState.IDLE



    # -------------------------------------------------
    # Inference
    # -------------------------------------------------

    def infer(
        self,
        facts,
    ):

        self.state = BrainState.INFERRING


        try:

            return self.inference_engine.infer(
                facts
            )


        finally:

            self.state = BrainState.IDLE



    # -------------------------------------------------
    # Reflection
    # -------------------------------------------------

    def reflect(
        self,
        facts,
    ):

        self.state = BrainState.REFLECTING


        try:

            return self.reflection_engine.reflect(
                facts
            )


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