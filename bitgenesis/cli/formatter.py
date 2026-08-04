from __future__ import annotations

from typing import Any


class ConsoleFormatter:
    """
    Formats BitGenesis console output.

    Responsible only for presentation.
    It does not execute commands or access runtime logic.
    """


    # ==================================================
    # Generic
    # ==================================================

    @staticmethod
    def title(
        text: str,
    ) -> str:

        return (
            "\n"
            + "=" * 50
            + "\n"
            + f" {text}"
            + "\n"
            + "=" * 50
        )



    @staticmethod
    def section(
        text: str,
    ) -> str:

        return (
            "\n"
            + text
            + "\n"
            + "-" * len(text)
        )



    # ==================================================
    # System
    # ==================================================

    @staticmethod
    def banner(
        version: str,
    ) -> str:

        return (
            "\n"
            "==============================================\n"
            f" BitGenesis Cognitive System v{version}\n"
            "==============================================\n"
            " Type '/help' for commands.\n"
            " Type '/exit' to shutdown.\n"
        )



    @staticmethod
    def status(
        data: dict[str, Any],
    ) -> str:

        lines = [
            "",
            "BitGenesis Status",
            "-----------------",
        ]


        for key, value in data.items():

            lines.append(
                f"{key}: {value}"
            )


        return "\n".join(
            lines
        )



    # ==================================================
    # Runtime
    # ==================================================

    @staticmethod
    def runtime(
        action: str,
        result=None,
    ) -> str:

        if result is None:

            return (
                f"Runtime {action} completed."
            )


        return (
            f"Runtime {action}:\n"
            f"{result}"
        )



    # ==================================================
    # Services
    # ==================================================

    @staticmethod
    def services(
        services,
    ) -> str:

        lines = [
            "",
            "Registered Services",
            "-------------------",
        ]


        if not services:

            lines.append(
                "No services registered."
            )


        else:

            for service in services:

                lines.append(
                    f"- {service}"
                )


        return "\n".join(
            lines
        )



    # ==================================================
    # Memory
    # ==================================================

    @staticmethod
    def memory(
        memories,
    ) -> str:

        lines = [
            "",
            "Memory Store",
            "------------",
        ]


        if not memories:

            lines.append(
                "No memories stored."
            )


        else:

            for index, memory in enumerate(
                memories,
                start=1,
            ):

                lines.append(
                    f"{index}. {memory}"
                )


        return "\n".join(
            lines
        )



    # ==================================================
    # Events
    # ==================================================

    @staticmethod
    def events(
        count: int,
    ) -> str:

        return (
            "\nEventBus\n"
            "--------\n"
            f"Subscribers: {count}"
        )



    # ==================================================
    # Errors
    # ==================================================

    @staticmethod
    def error(
        message: str,
    ) -> str:

        return (
            f"[ERROR] {message}"
        )



    @staticmethod
    def unknown_command(
        command: str,
    ) -> str:

        return (
            f"Unknown command: {command}"
        )