import traceback
from flask import Flask, request, abort
from uuid import uuid4

app = Flask(__name__)
stats = {"num_todos_added": 0, "num_todos_removed": 0}


@app.route('/stats', methods=["GET"])
def get_stats():
    return stats

@app.route('/stats', methods=["POST"])
def todo_added():
    stats["num_todos_added"] = stats["num_todos_added"] + 1
    return stats


@app.route('/stats', methods=["DELETE"])
def todo_removed():
    stats["num_todos_removed"] = stats["num_todos_removed"] + 1
    return stats
