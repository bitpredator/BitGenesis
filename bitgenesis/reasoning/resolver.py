from bitgenesis.identity.query import IdentityQuery
from bitgenesis.memory.query import MemoryQuery
from bitgenesis.reasoning.resolution import Resolution


class Resolver:

    def __init__(self, memory_store=None):

        self.identity = IdentityQuery()
        self.memory = MemoryQuery(memory_store) if memory_store else None

        self._domains = {}

        self.register("identity", self._resolve_identity)
        self.register("memory", self._resolve_memory)

    def register(self, domain, handler):

        self._domains[domain] = handler

    def resolve(self, intent):

        if intent is None:
            return None

        handler = self._domains.get(intent.domain)

        if handler is None:
            return None

        return handler(intent)

    # --------------------------
    # IDENTITY
    # --------------------------

    def _resolve_identity(self, intent):

        value = self.identity.field(intent.target)

        return Resolution(
            domain=intent.domain,
            target=intent.target,
            value=value,
        )

    # --------------------------
    # MEMORY
    # --------------------------

    def _resolve_memory(self, intent):

        if self.memory is None:
            return None


        # --------------------------
        # MEMORY SEARCH
        # --------------------------

        if intent.action == "search":

            value = self.memory.search_text(
                intent.target
            )


        # --------------------------
        # MEMORY QUERY
        # --------------------------

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