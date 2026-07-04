from bitgenesis.reasoning.engine import ReasoningEngine
from bitgenesis.reasoning.context_fusion import ContextFusion
from bitgenesis.reasoning.context import ReasoningContext
from bitgenesis.planning.planner import Planner
from bitgenesis.runtime.executor import Executor


class ReasoningSession:

    def __init__(self, memory_store):

        self.memory_store = memory_store

        self.engine = ReasoningEngine()
        self.fusion = ContextFusion()
        self.planner = Planner()

        # 🔥 FIX: executor finalmente collegato
        self.executor = Executor(
            memory_store=memory_store
        )

    def process(self, event):

        # 1. FUSION
        unified = self.fusion.build(
            event=event,
            memory_store=self.memory_store,
        )

        context = ReasoningContext(unified=unified)

        # 2. DECISION
        decision = self.engine.evaluate(context)

        # 3. PLANNING
        plan = self.planner.build(decision, context)

        decision.plan = plan

        # 4. EXECUTION (MISSING PIECE ORA RISOLTA)
        execution_result = self.executor.execute(
            plan=plan,
            decision=decision,
            event=event,
        )

        # 5. ATTACH RESULT
        decision.execution = execution_result

        return decision