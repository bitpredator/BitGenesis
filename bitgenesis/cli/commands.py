from __future__ import annotations


class CLICommand:

    def __init__(
        self,
        raw: str,
    ):

        self.raw = raw.strip()

        parts = self.raw.split()

        self.name = (
            parts[0].lower()
            if parts
            else ""
        )

        self.args = [
            x.lower()
            for x in parts[1:]
        ]


    def has(
        self,
        value: str,
    ) -> bool:

        return value.lower() in self.args



    def argument(
        self,
        index: int,
        default=None,
    ):

        try:

            return self.args[index]

        except IndexError:

            return default