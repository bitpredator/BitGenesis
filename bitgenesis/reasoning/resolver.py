from bitgenesis.identity.query import IdentityQuery


class Resolver:

    def __init__(self):

        self._domains = {}

        self.register(
            "identity",
            self._resolve_identity,
        )

    def register(self, domain, handler):

        self._domains[domain] = handler

    def resolve(self, intent):

        if intent is None:
            return None

        handler = self._domains.get(intent.domain)

        if handler is None:
            return None

        return handler(intent)

    def _resolve_identity(self, intent):

        query = IdentityQuery()

        return query.field(intent.target)