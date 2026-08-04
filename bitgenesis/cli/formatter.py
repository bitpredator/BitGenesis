from __future__ import annotations



class CLIFormatter:
    """
    Formats BitGenesis CLI output.
    """


    @staticmethod
    def title(
        text: str,
    ) -> str:

        return (
            f"\n{text}\n"
            f"{'-' * len(text)}"
        )



    @staticmethod
    def learning(
        statistics: dict,
    ) -> str:
        """
        Formats learning statistics.
        """


        lines = [

            "Learning Statistics",

            "-------------------",

            f"Experiences: {statistics.get('total', 0)}",

            f"Successful: {statistics.get('successful', 0)}",

            f"Failed: {statistics.get('failed', 0)}",

            (
                f"Success rate: "
                f"{statistics.get('success_rate', 0) * 100:.2f}%"
            ),

            "",

            "States:",
        ]


        states = statistics.get(
            "states",
            {},
        )


        if not states:

            lines.append(
                "- none"
            )

        else:

            for state, count in states.items():

                lines.append(
                    f"- {state}: {count}"
                )


        return "\n".join(
            lines
        )