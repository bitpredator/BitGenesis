from __future__ import annotations


from bitgenesis.dialogue.formatters.identity_formatter import (
    IdentityFormatter,
)

from bitgenesis.dialogue.formatters.memory_formatter import (
    MemoryFormatter,
)


from bitgenesis.language.detector import Language



class ResponseFormatter:
    """
    Main response formatter dispatcher.

    Routes resolutions to domain-specific formatters
    while preserving language context.
    """



    def __init__(self):

        self._formatters = {

            "identity": IdentityFormatter(),

            "memory": MemoryFormatter(),

        }



    def register(
        self,
        domain,
        formatter,
    ):

        self._formatters[domain] = formatter



    def format(
        self,
        resolution,
        language: Language | None = None,
    ):

        if resolution is None:

            return None



        formatter = self._formatters.get(
            resolution.domain
        )



        if formatter is None:

            return str(
                resolution.value
            )



        # Pass language only to formatters
        # supporting multilingual output.

        try:

            return formatter.format(
                resolution,
                language=language,
            )


        except TypeError:

            # Backwards compatibility with
            # old formatters.

            return formatter.format(
                resolution
            )