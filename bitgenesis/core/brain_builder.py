from __future__ import annotations


from bitgenesis.core.brain import Brain
from bitgenesis.core.config import BrainConfig


from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.storage.json_backend import JsonMemoryBackend
from bitgenesis.memory.storage.in_memory_backend import InMemoryBackend


from bitgenesis.knowledge.registry import KnowledgeRegistry
from bitgenesis.knowledge.core import CoreKnowledge


from bitgenesis.runtime.runtime_manager import RuntimeManager
from bitgenesis.events.event_bus import EventBus



class BrainBuilder:
    """
    Builder responsible for creating a fully configured Brain.

    Keeps construction logic outside the Brain class.
    """


    def __init__(
        self,
        config: BrainConfig | None = None,
    ):

        self.config = (
            config
            or BrainConfig()
        )


        self._event_bus = None

        self._runtime = None

        self._memory_store = None

        self._knowledge = None



    # -------------------------------------------------
    # Services
    # -------------------------------------------------


    def with_event_bus(
        self,
        event_bus,
    ):

        self._event_bus = event_bus

        return self



    def with_runtime(
        self,
        runtime,
    ):

        self._runtime = runtime

        return self



    def with_memory(
        self,
        memory_store,
    ):

        self._memory_store = memory_store

        return self



    def with_knowledge(
        self,
        knowledge,
    ):

        self._knowledge = knowledge

        return self



    # -------------------------------------------------
    # Default services
    # -------------------------------------------------


    def build_memory(
        self,
    ):

        if self.config.memory_backend == "json":

            backend = JsonMemoryBackend(
                self.config.memory_path
            )

        else:

            backend = InMemoryBackend()



        return MemoryStore(
            backend=backend
        )



    def build_event_bus(
        self,
    ):

        return EventBus()



    def build_runtime(
        self,
    ):

        return RuntimeManager()



    def build_knowledge(
        self,
    ):

        return KnowledgeRegistry()



    # -------------------------------------------------
    # Core knowledge
    # -------------------------------------------------


    def initialize_core_knowledge(
        self,
        knowledge: KnowledgeRegistry,
    ):
        """
        Loads BitGenesis built-in knowledge.
        """


        CoreKnowledge(
            knowledge
        ).load()



    # -------------------------------------------------
    # Build
    # -------------------------------------------------


    def build(
        self,
    ):


        memory = (

            self._memory_store

            or self.build_memory()

        )



        event_bus = (

            self._event_bus

            or self.build_event_bus()

        )



        runtime = (

            self._runtime

            or self.build_runtime()

        )



        knowledge = (

            self._knowledge

            or self.build_knowledge()

        )



        # ---------------------------------------------
        # Load innate knowledge
        # ---------------------------------------------


        self.initialize_core_knowledge(
            knowledge
        )



        return Brain(

            config=self.config,

            event_bus=event_bus,

            runtime=runtime,

            memory_store=memory,

            knowledge=knowledge,

        )