class EpisodeTitleGenerator:

    def generate(self, memories):

        if not memories:
            return "Empty Episode"

        text = " ".join(
            (
                memory.content
                .get("payload", {})
                .get("message", "")
            ).lower()
            for memory in memories
        )

        # priorità dalla più specifica alla più generale

        if "planner" in text:
            return "Planner Episode"

        if "system" in text:
            return "System Startup"

        if "user" in text:
            return "User Preferences"

        if "memory" in text:
            return "Memory Episode"

        return "General Episode"