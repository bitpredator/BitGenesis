from bitgenesis.identity.query import IdentityQuery

from bitgenesis.memory.query import MemoryQuery

from bitgenesis.reasoning.resolution import Resolution



class Resolver:
    """
    Resolves cognitive intents into structured resolutions.

    Supported domains:

    - identity
    - memory
    - knowledge
    - unknown
    """



    def __init__(
        self,
        memory_store=None,
        knowledge_registry=None,
    ):


        self.identity = IdentityQuery()



        self.memory = (

            MemoryQuery(memory_store)

            if memory_store

            else None
        )



        self.knowledge = knowledge_registry



        self._domains = {}



        self.register(
            "identity",
            self._resolve_identity
        )


        self.register(
            "memory",
            self._resolve_memory
        )


        self.register(
            "knowledge",
            self._resolve_knowledge
        )


        self.register(
            "unknown",
            self._resolve_unknown
        )



    # ==================================================
    # Registration
    # ==================================================


    def register(
        self,
        domain,
        handler,
    ):

        self._domains[domain] = handler



    # ==================================================
    # Resolve
    # ==================================================


    def resolve(
        self,
        intent,
    ):


        if intent is None:

            return None



        handler = self._domains.get(
            intent.domain
        )



        if handler is None:

            return None



        return handler(
            intent
        )



    # ==================================================
    # Identity
    # ==================================================


    def _resolve_identity(
        self,
        intent,
    ):


        value = self.identity.field(
            intent.target
        )



        return Resolution(

            domain=intent.domain,

            target=intent.target,

            value=value,

        )



    # ==================================================
    # Memory
    # ==================================================


    def _resolve_memory(
        self,
        intent,
    ):


        if self.memory is None:

            return None



        if intent.action == "search":


            value = self.memory.search_text(
                intent.target
            )



        elif intent.target == "latest":


            value = self.memory.latest()



        elif intent.target == "recent":


            value = self.memory.recent()



        else:


            value = self.memory.all()



        return Resolution(

            domain=intent.domain,

            target=intent.target,

            value=value,

        )



    # ==================================================
    # Knowledge
    # ==================================================


    def _resolve_knowledge(
        self,
        intent,
    ):


        if self.knowledge is None:

            return None



        entity = self.knowledge.get(
            intent.target
        )



        if entity is None:

            return None



        return Resolution(

            domain="knowledge",

            target=intent.target,

            value=entity,

        )



    # ==================================================
    # Unknown
    # ==================================================


    def _resolve_unknown(
        self,
        intent,
    ):


        return Resolution(

            domain="unknown",

            target=intent.target,

            value=(

                "I do not have enough knowledge "
                "about this subject yet. "
                "This experience could become "
                "part of my future learning process."

            ),

        )