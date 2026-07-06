class MemoryRetrieval:

    def search(self, memories, query: str):

        if not query:
            return []

        normalized = query.lower().strip()

        if not normalized:
            return []

        results = []

        for memory in memories:

            message = (
                memory.content
                .get("payload", {})
                .get("message", "")
            )

            if not isinstance(message, str):
                continue

            if normalized in message.lower():

                results.append(memory)

        return results