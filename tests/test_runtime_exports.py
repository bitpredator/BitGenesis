from bitgenesis import runtime


def test_runtime_public_exports():

    exports = runtime.__all__


    expected = [
        "ExecutionStep",
        "ExecutionPlan",
        "CognitiveExecutionPlanner",
        "PlannerResult",
        "ServiceContext",
        "ServiceExecution",
        "OrchestrationResult",
        "ServiceDescriptor",
        "ServiceRegistry",
        "ServiceOrchestrator",
        "RuntimeMetrics",
        "RuntimeStatistics",
        "RuntimeSnapshot",
    ]


    for item in expected:

        assert item in exports
        assert hasattr(runtime, item)