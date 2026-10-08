from src.agent.state import AgentState


def test_state_creation():
    state = AgentState(goal="Find a running shoe under 5000 INR")

    assert state.goal == "Find a running shoe under 5000 INR"
    assert state.iteration == 0
    assert state.observations == []
    assert state.actions == []
    assert state.status == "IN_PROGRESS"


def test_add_action():
    state = AgentState(goal="Find a running shoe under 5000 INR")

    state.add_action("get_product(P1001)")

    assert state.actions == ["get_product(P1001)"]


def test_add_observation():
    state = AgentState(goal="Find a running shoe under 5000 INR")

    state.add_observation("P1001 is a running shoe")

    assert state.observations == ["P1001 is a running shoe"]


def test_iteration_update():
    state = AgentState(goal="Find a running shoe under 5000 INR")

    state.increment_iteration()
    state.increment_iteration()

    assert state.iteration == 2


def test_status_update():
    state = AgentState(goal="Find a running shoe under 5000 INR")

    state.update_status("COMPLETED")

    assert state.status == "COMPLETED"