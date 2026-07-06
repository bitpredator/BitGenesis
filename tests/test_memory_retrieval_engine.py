from bitgenesis.memory.retrieval import MemoryRetrieval


class FakeMemory:

    def __init__(self, message):

        self.content = {
            "payload": {
                "message": message
            }
        }



def test_retrieval_returns_matching_memories():

    memories = [
        FakeMemory("Python module created"),
        FakeMemory("Planner initialized"),
        FakeMemory("Memory subsystem ready"),
    ]

    retrieval = MemoryRetrieval()

    result = retrieval.search(
        memories,
        "python"
    )

    assert len(result) == 1
    assert (
        result[0]
        .content["payload"]["message"]
        ==
        "Python module created"
    )



def test_retrieval_is_case_insensitive():

    memories = [
        FakeMemory("Python module created"),
    ]

    retrieval = MemoryRetrieval()

    result = retrieval.search(
        memories,
        "PYTHON"
    )

    assert len(result) == 1



def test_retrieval_returns_empty_when_not_found():

    memories = [
        FakeMemory("Planner initialized"),
    ]

    retrieval = MemoryRetrieval()

    result = retrieval.search(
        memories,
        "database"
    )

    assert result == []