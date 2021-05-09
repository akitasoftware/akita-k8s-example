import json
import os
import redis
import requests
import traceback
from flask import Flask, request, abort
from uuid import uuid4

# Configurations
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
STAT_SERVICE_URL = os.getenv("STAT_SERVICE_URL", "http://localhost:5001/stats")

# Data store setup
dataStore = redis.Redis(host=REDIS_HOST, port=6379, db=0)

# REST API
app = Flask(__name__)


@app.route('/todos', methods=["GET"])
def list_todos():
    todos = [json.loads(item) for item in dataStore.hgetall("todos").values()]
    return {"todos": todos}


@app.route('/todos', methods=["POST"])
def create_todo():
    try:
        new_todo = _validate_new_todo(request.get_json())
        dataStore.hset("todos", new_todo["id"], json.dumps(new_todo))
        requests.post(STAT_SERVICE_URL)
        return new_todo
    except Exception as e:
        traceback.print_exc()
        abort(400)


@app.route('/todos/<todo_id>', methods=["DELETE"])
def delete_todo(todo_id):
    try:
        dataStore.hdel("todos", todo_id)
        requests.delete(STAT_SERVICE_URL)
        return '', 204
    except Exception as e:
        traceback.print_exc()
        abort(404)


def _validate_new_todo(new_todo):
    name = new_todo.get("name", None)
    description = new_todo.get("description", None)
    if name is None or len(name) == 0:
        raise Exception("name is required")
    if description is None or len(description) == 0:
        raise Exception("description is required")

    return {
        "id": uuid4().__str__(),
        "name": new_todo["name"],
        "description": new_todo["description"]
    }
