def todo_serializer(todo) -> dict:
    return {
        "id":str(todo["_id"]),
        "title":todo["title"],
        "description":todo["description"],
        "status":todo["status"],
        "date":todo["date"]

    }
def todos_serializer(todos) -> list:
    return [todo_serializer(todo) for todo in todos]
