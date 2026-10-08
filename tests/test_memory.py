from src.memory.memory_store import MemoryStore, build_memory_context


def test_memory_creates_default_value(tmp_path):
    memory = MemoryStore(tmp_path / "memory.json")

    assert memory.read() == {}


def test_memory_writes_a_preference(tmp_path):
    file_path = tmp_path / "memory.json"

    memory = MemoryStore(file_path)
    memory.write("user_budget_preference", "5000 INR")

    assert memory.read() == {
        "user_budget_preference": "5000 INR"
    }


def test_memory_updates_an_existing_preference(tmp_path):
    file_path = tmp_path / "memory.json"

    memory = MemoryStore(file_path)
    memory.write("user_budget_preference", "5000 INR")
    memory.write("user_budget_preference", "4000 INR")

    assert memory.read()["user_budget_preference"] == "4000 INR"


def test_memory_creates_missing_directory(tmp_path):
    file_path = tmp_path / "nested" / "memory.json"

    memory = MemoryStore(file_path)
    memory.write("user_budget_preference", "5000 INR")

    assert file_path.exists()


def test_memory_can_support_a_new_task(tmp_path):
    file_path = tmp_path / "memory.json"

    memory = MemoryStore(file_path)
    memory.write("user_budget_preference", "5000 INR")

    context = build_memory_context(memory)

    assert context == "The user prefers products under 5000 INR."