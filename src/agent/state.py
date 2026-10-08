from dataclasses import dataclass, field


@dataclass
class AgentState:
    """The current execution context for one agent task."""

    goal: str
    iteration: int = 0
    observations: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    status: str = "IN_PROGRESS"

    def add_action(self, action: str) -> None:
        self.actions.append(action)

    def add_observation(self, observation: str) -> None:
        self.observations.append(observation)

    def increment_iteration(self) -> None:
        self.iteration += 1

    def update_status(self, status: str) -> None:
        self.status = status