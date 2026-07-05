from bitgenesis.identity.query import IdentityQuery
from bitgenesis.reasoning.resolution import Resolution


class Resolver:

    def __init__(self):

        self._domains = {}

        self.register("identity", self._resolve_identity)

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
    # IDENTITY DOMAIN
    # --------------------------
    def _resolve_identity(self, intent):

        query = IdentityQuery()

        value = query.field(intent.target)

        return Resolution(
            domain=intent.domain,
            target=intent.target,
            value=value,
        )