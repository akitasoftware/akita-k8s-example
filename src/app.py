import traceback
from flask import Flask, request, abort
from uuid import uuid4

app = Flask(__name__)
inMemTodoStore = {}


@app.route('/todos', methods=["GET"])
def list_todos():
    todos = [todo[1] for todo in inMemTodoStore.items()]
    print(inMemTodoStore)
    return {"todos": todos}


@app.route('/todos', methods=["POST"])
def create_todo():
    try:
        new_todo = _validate_new_todo(request.get_json())
        inMemTodoStore[new_todo["id"].__str__()] = new_todo
        return new_todo
    except Exception as e:
        traceback.print_exc(e)
        abort(400)


@app.route('/todos/<todo_id>', methods=["DELETE"])
def delete_todo(todo_id):
    try:
        inMemTodoStore.pop(todo_id)
        return '', 204
    except Exception as e:
        traceback.print_exc(e)
        abort(404)


def create_todo():
    try:
        new_todo = _validate_new_todo(request.get_json())
        inMemTodoStore.append(new_todo)
        return new_todo
    except Exception as e:
        traceback.print_exc(e)
        abort(400)


def _validate_new_todo(new_todo):
    name = new_todo.get("name", None)
    description = new_todo.get("description", None)
    if name is None or len(name) == 0:
        raise Exception("name is required")
    if description is None or len(description) == 0:
        raise Exception("description is required")

    return {
        "id": uuid4(),
        "name": new_todo["name"],
        "description": new_todo["description"]
    }
