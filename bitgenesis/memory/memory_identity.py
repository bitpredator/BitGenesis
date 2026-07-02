# bitgenesis/memory/memory_identity.py

class MemoryIdentity:

    CREATOR = "BitGenesis Core System"

    ORIGIN_STORY = (
        "This system was created as part of the BitGenesis project, "
        "a modular cognitive memory architecture designed for event-driven learning."
    )

    @staticmethod
    def inject(memory):

        if memory.metadata is None:
            memory.metadata = {}

        # identity injection (idempotent)
        memory.metadata.setdefault("creator", MemoryIdentity.CREATOR)
        memory.metadata.setdefault("origin", MemoryIdentity.ORIGIN_STORY)

        if "identity" not in memory.tags:
            memory.tags.append("identity")

        return memory