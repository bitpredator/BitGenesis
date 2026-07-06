from bitgenesis.reasoning.resolution import Resolution


class MemoryFormatter:

    def format(self, resolution: Resolution):

        value = resolution.value

        if value is None:
            return "I don't remember anything."

        if isinstance(value, list):

            if not value:
                return "I don't remember anything."

            lines = []

            for memory in value:

                if not hasattr(memory, "content"):
                    lines.append(str(memory))
                    continue

                message = (
                    memory.content
                    .get("payload", {})
                    .get("message")
                )

                if message:
                    lines.append(f"• {message}")
                else:
                    lines.append(str(memory))

            return "I currently remember:\n\n" + "\n".join(lines)

        if not hasattr(value, "content"):
            return str(value)

        message = (
            value.content
            .get("payload", {})
            .get("message")
        )

        if message:
            return f"My latest memory is:\n{message}"

        return str(value)