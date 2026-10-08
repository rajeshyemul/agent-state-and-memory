from src.agent.runner import AgentRunner
from src.agent.state import AgentState


def test_runner_creates_initial_state():
    runner = AgentRunner(
        goal="Find a running shoe under 5000 INR",
        decide_action=lambda state: "get_product(P1001)",
        execute_action=lambda action: "P1001 is a running shoe",
        is_complete=lambda state, action, observation: False,
        max_iterations=1,
    )

    state = runner.run()

    assert isinstance(state, AgentState)
    assert state.goal == "Find a running shoe under 5000 INR"
    assert state.iteration == 1
    assert state.actions == ["get_product(P1001)"]
    assert state.observations == ["P1001 is a running shoe"]
    assert state.status == "FAILED"

def test_runner_marks_state_complete():
    actions = iter(["get_product(P1001)", "finish"])

    def decide_action(state):
        return next(actions)

    def execute_action(action):
        return "Found a suitable option" if action == "finish" else "P1001 is a running shoe"

    runner = AgentRunner(
        goal="Find a running shoe under 5000 INR",
        decide_action=decide_action,
        execute_action=execute_action,
        is_complete=lambda state, action, observation: action == "finish",
    )

    state = runner.run()

    assert state.iteration == 2
    assert state.status == "COMPLETED"

def test_runner_stops_after_max_iterations():
    runner = AgentRunner(
        goal="Find a running shoe under 5000 INR",
        decide_action=lambda state: "get_product(P1001)",
        execute_action=lambda action: "P1001 is a running shoe",
        is_complete=lambda state, action, observation: False,
        max_iterations=3,
    )

    state = runner.run()

    assert state.iteration == 3
    assert state.status == "FAILED"