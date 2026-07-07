class InferenceRules:

    def apply(self, facts):

        if not facts:
            return []

        inferred = []

        facts = list(dict.fromkeys(facts))

        is_a = []
        likes = []

        for fact in facts:

            parts = str(fact).split()

            if len(parts) != 3:
                continue

            subject, predicate, obj = parts

            if predicate == "is_a":
                is_a.append((subject, obj))

            elif predicate == "likes":
                likes.append((subject, obj))

        for entity, parent in is_a:

            for subject, liked in likes:

                if liked != entity:
                    continue

                new_fact = (
                    f"{subject} likes {parent}"
                )

                if (
                    new_fact not in facts
                    and new_fact not in inferred
                ):
                    inferred.append(new_fact)

        return inferred