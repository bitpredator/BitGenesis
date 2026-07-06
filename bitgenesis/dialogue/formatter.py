from bitgenesis.dialogue.formatters.identity_formatter import IdentityFormatter
from bitgenesis.dialogue.formatters.memory_formatter import MemoryFormatter


class ResponseFormatter:

    def __init__(self):

        self._formatters = {
            "identity": IdentityFormatter(),
            "memory": MemoryFormatter(),
        }

    def register(self, domain, formatter):

        self._formatters[domain] = formatter

    def format(self, resolution):

        if resolution is None:
            return None

        formatter = self._formatters.get(resolution.domain)

        if formatter is None:
            return str(resolution.value)

        return formatter.format(resolution)