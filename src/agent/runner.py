from src.agent.state import AgentState

class AgentRunner:
    def __init__(
        self,
        goal,
        decide_action,
        execute_action,
        is_complete,
        max_iterations=10,
    ):
        self.goal = goal
        self.decide_action = decide_action
        self.execute_action = execute_action
        self.is_complete = is_complete
        self.max_iterations = max_iterations

    def run(self):
        state = AgentState(goal=self.goal)

        while state.status == "IN_PROGRESS":
            if state.iteration >= self.max_iterations:
                state.update_status("FAILED")
                break

            action = self.decide_action(state)
            state.add_action(action)

            observation = self.execute_action(action)
            state.add_observation(observation)

            state.increment_iteration()

            if self.is_complete(state, action, observation):
                state.update_status("COMPLETED")
                break

        return state