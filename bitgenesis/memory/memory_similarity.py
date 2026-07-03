class MemorySimilarity:

    @staticmethod
    def score(payload1, payload2):
        """
        Computes a deterministic similarity score between two payloads.

        Scoring:
        +1 -> same key exists
        +2 -> same value for the same key

        Returns:
            float
        """

        if not isinstance(payload1, dict):
            return 0.0

        if not isinstance(payload2, dict):
            return 0.0

        score = 0.0

        for key, value in payload1.items():

            if key not in payload2:
                continue

            # stessa chiave
            score += 1.0

            # stesso valore
            if payload2[key] == value:
                score += 2.0

        return score