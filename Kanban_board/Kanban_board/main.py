from flask import jsonify, request, Blueprint
from flask_cors import CORS  # Import CORS
from . import db
from .models import Task

main = Blueprint("main", __name__)
CORS(main)  # Enable CORS for the main blueprint


@main.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    tasks_list = [{"id": task.id, "title": task.title, "column": task.column} for task in tasks]
    return jsonify(tasks_list)


@main.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    title = data.get("title")
    new_task = Task(title=title, column="To Do")
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id, "title": new_task.title, "column": new_task.column}), 201


@main.route("/api/move/<int:id>/<string:direction>", methods=["POST"])
def move(id, direction):
    task = Task.query.get(id)
    if direction == "right":
        if task.column == "To Do":
            task.column = "In Progress"
        elif task.column == "In Progress":
            task.column = "Done"
    elif direction == "left":
        if task.column == "Done":
            task.column = "In Progress"
        elif task.column == "In Progress":
            task.column = "To Do"
    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "column": task.column})

