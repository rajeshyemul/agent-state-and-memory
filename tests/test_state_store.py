from src.agent.state import AgentState
from src.state.state_store import StateStore


def test_save_and_load_state(tmp_path):
    file_path = tmp_path / "state.json"

    state = AgentState(
        goal="Find a running shoe under 5000 INR",
        iteration=2,
        actions=["get_product(P1001)"],
        observations=["P1001 is a running shoe"],
        status="IN_PROGRESS",
    )

    store = StateStore(file_path)
    store.save(state)

    loaded_state = store.load()

    assert loaded_state == state


def test_save_creates_missing_directory(tmp_path):
    file_path = tmp_path / "nested" / "state.json"

    store = StateStore(file_path)
    store.save(
        AgentState(
            goal="Find a running shoe under 5000 INR",
        )
    )

    assert file_path.exists()


def test_load_returns_state_from_file(tmp_path):
    file_path = tmp_path / "state.json"

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        """
        {
            "goal": "Find a running shoe under 5000 INR",
            "iteration": 1,
            "observations": ["P1001 is a running shoe"],
            "actions": ["get_product(P1001)"],
            "status": "IN_PROGRESS"
        }
        """,
        encoding="utf-8",
    )

    store = StateStore(file_path)
    loaded_state = store.load()

    assert loaded_state.goal == "Find a running shoe under 5000 INR"
    assert loaded_state.iteration == 1
    assert loaded_state.actions == ["get_product(P1001)"]
    assert loaded_state.observations == ["P1001 is a running shoe"]
    assert loaded_state.status == "IN_PROGRESS"