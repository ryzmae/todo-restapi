def invidual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

def list_serial(todos) -> list:
    return [invidual_serial(todo) for todo in todos]