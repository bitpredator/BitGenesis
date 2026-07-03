from dataclasses import dataclass
from typing import Any


@dataclass
class UnifiedContext:
    event: Any
    memory_context: Any
    knowledge_context: Any
    attention: Any | None = None


class ContextFusion:

    def __init__(self, memory_attention=None, knowledge_query=None):

        self.memory_attention = memory_attention
        self.knowledge_query = knowledge_query

    def build(self, event, memory_store):

        # 1. MEMORY CONTEXT
        memories = memory_store.all()

        if self.memory_attention:
            memories = self.memory_attention.select(memories)

        memory_context = {
            "items": memories
        }

        # 2. KNOWLEDGE CONTEXT
        knowledge_context = None

        if self.knowledge_query and hasattr(event, "subject"):

            knowledge_context = {
                "relations": self.knowledge_query.relations_of(event.subject)
            }

        # 3. FUSION
        return UnifiedContext(
            event=event,
            memory_context=memory_context,
            knowledge_context=knowledge_context,
            attention=memories,
        )