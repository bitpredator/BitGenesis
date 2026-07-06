from typing import List


class MemoryQuery:

    def __init__(self, memory_store):

        self.memory_store = memory_store

    def all(self) -> List:

        return list(self.memory_store.all())

    def recent(self, limit: int = 5) -> List:

        memories = list(self.memory_store.all())

        return memories[-limit:]

    def latest(self):

        memories = list(self.memory_store.all())

        if not memories:
            return None

        return memories[-1]

    def search(self, predicate):

        return [
            memory
            for memory in self.memory_store.all()
            if predicate(memory)
        ]

    def search_text(self, text: str):

        text = text.lower().strip()

        if not text:
            return []

        def matches(memory):

            message = (
                memory.content
                .get("payload", {})
                .get("message", "")
            )

            if not isinstance(message, str):
                return False

            return text in message.lower()

        return self.search(matches)