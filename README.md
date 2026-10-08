# Agent State and Memory

[![GitHub Repository](https://img.shields.io/badge/GitHub-agent--state--and--memory-181717?logo=github)](https://github.com/rajeshyemul/agent-state-and-memory)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-16%20passing-4c1?logo=pytest&logoColor=white)](https://github.com/rajeshyemul/agent-state-and-memory)

A small learning project that demonstrates the difference between:

- **Agent state:** the current execution context for one task
- **Persistent state:** the saved state that can be resumed after interruption
- **Memory:** reusable information retained across future tasks

The project intentionally uses simple JSON files rather than databases, embeddings, or external services.

## Learning Objectives

1. Represent the agent's current execution state explicitly.
2. Keep the state synchronized with every action and observation.
3. Use a state-aware agent loop.
4. Save and restore state for checkpointing and resumability.
5. Store reusable preferences separately from the current task state.

## Project Structure

```text
.
├── .agent/
│   ├── memory.json
│   └── state.json
├── docs/
├── src/
│   ├── agent/
│   │   ├── runner.py
│   │   └── state.py
│   ├── memory/
│   │   └── memory_store.py
│   └── state/
│       └── state_store.py
├── tests/
│   ├── test_agent_loop.py
│   ├── test_memory.py
│   ├── test_state.py
│   └── test_state_store.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup

### 1. Create and activate a virtual environment

```bash
cd "/Users/rajesh.yemul/Practice Project/05-agent-state-and-memory"
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Run the tests

```bash
python -m pytest -q
```

## Current Behavior

The project stores:

- The current task goal, actions, observations, iteration, and status in the agent state.
- The current task checkpoint in `.agent/state.json`.
- Reusable preferences in `.agent/memory.json`.

The state and memory are intentionally separate:

```text
STATE: What is happening right now?
MEMORY: What should be remembered for later?
```

## State Lifecycle

```text
Create state
    ↓
Decide action
    ↓
Record action
    ↓
Execute action
    ↓
Record observation
    ↓
Increment iteration
    ↓
Check completion
    ↓
Save checkpoint
    ↓
Continue or finish
```

## Memory Example

A user preference such as `5000 INR` is written to the memory store:

```python
from src.memory.memory_store import MemoryStore

memory = MemoryStore()
memory.write("user_budget_preference", "5000 INR")
```

The stored information can later be used as context for another task without changing the current execution state.

## Testing

The project uses pytest. The full suite is intended to validate state, agent-loop behavior, persistence, and memory independently.

```bash
python -m pytest -q
```

## Notes

- This project is a conceptual learning implementation.
- It uses local JSON files rather than a database.
- It intentionally avoids vector databases, embeddings, and external memory systems for now.
- The `.venv` directory should not be committed to Git.
