from pathlib import Path
import json


class MemoryStore:
    def __init__(self, file_path: str | Path = ".agent/memory.json"):
        self.file_path = Path(file_path)

    def read(self):
        if not self.file_path.exists():
            return {}

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, key: str, value):
        memory = self.read()

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        memory[key] = value

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(memory, file, indent=2)

        return memory


def build_memory_context(memory: MemoryStore) -> str:
    """Create a short natural-language context from saved preferences."""
    stored_memory = memory.read()
    preference = stored_memory.get("user_budget_preference")

    if preference is None:
        return "No reusable user preference is available."

    return f"The user prefers products under {preference}."