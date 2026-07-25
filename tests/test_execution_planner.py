from bitgenesis.runtime.planner import CognitiveExecutionPlanner
from bitgenesis.runtime.execution_plan import ExecutionPlan
from bitgenesis.runtime.planner_result import PlannerResult



class Decision:

    def __init__(
        self,
        action,
    ):

        self.action = action



def test_planner_creates_execution_plan():

    planner = CognitiveExecutionPlanner()


    result = planner.create_plan(
        Decision(
            "store_memory"
        )
    )


    assert result.success


    assert len(
        result.plan.steps
    ) == 1


    assert (
        result.plan.steps[0].action
        == "store_memory"
    )



def test_planner_rejects_empty_decision():

    planner = CognitiveExecutionPlanner()


    result = planner.create_plan(
        None
    )


    assert not result.success


    assert result.plan.empty()



def test_planner_rejects_missing_action():

    class InvalidDecision:
        pass


    planner = CognitiveExecutionPlanner()


    result = planner.create_plan(
        InvalidDecision()
    )


    assert not result.success

    assert result.reason == "missing action"
    

def test_planner_result_contains_plan():

    plan = ExecutionPlan()


    result = PlannerResult(
        success=True,
        plan=plan,
    )


    assert result.success

    assert result.plan is plan