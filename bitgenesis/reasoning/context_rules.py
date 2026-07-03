class ContextAwareRules:

    @staticmethod
    def score_memory(memory_context):

        if not memory_context or not memory_context.get("items"):
            return 0.0

        items = memory_context["items"]

        score = 0.0

        for m in items:
            score += getattr(m, "importance", 0.5) * 0.6
            score += getattr(m, "confidence", 0.5) * 0.4

        return min(score / len(items), 1.0)

    @staticmethod
    def score_knowledge(knowledge_context):

        if not knowledge_context or not knowledge_context.get("relations"):
            return 0.0

        relations = knowledge_context["relations"]

        # più relazioni = più rilevanza
        return min(len(relations) * 0.2, 1.0)

    @staticmethod
    def decide(memory_score, knowledge_score):

        if knowledge_score > memory_score and knowledge_score > 0.3:
            return "use_knowledge"

        if memory_score > 0:
            return "use_memory"

        return "ignore"