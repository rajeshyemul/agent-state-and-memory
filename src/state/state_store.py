from pathlib import Path
import json

from src.agent.state import AgentState


class StateStore:
    def __init__(self, file_path: str | Path= ".agent/state.json"):
        self.file_path = Path(file_path)

    def save(self, state: AgentState) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                {
                    "goal": state.goal,
                    "iteration": state.iteration,
                    "observations": state.observations,
                    "actions": state.actions,
                    "status": state.status,
                },
                file,
                indent=2,
            )

    def load(self) -> AgentState:
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return AgentState(
            goal=data["goal"],
            iteration=data["iteration"],
            observations=data["observations"],
            actions=data["actions"],
            status=data["status"],
        )