from flask import Blueprint, request
from todos.models import Task, NewTaskSchema
from marshmallow import ValidationError
from db import db
import jwt, os, datetime
from utils.auth import login, authorized
from utils.bcrypt import bcrypt


todos_bp = Blueprint("todos", __name__)


# Get All Tasks
@todos_bp.route("", methods=["GET"])
@login
def get_todos(user_id, username, role):
    if role == "manager":
        todos = [
            {
                "_id": task._id,
                "title": task.title,
                "content": task.content,
                "priority": task.priority.value,
                "status": task.status.value,
                "dueDates": task.dueDates,
                "assignor": task.assignor,
                "assignee": task.assignee,
                "user_id": task.user_id,
                "dateCreated": task.dateCreated,
            }
            for task in Task.query.all()
        ]
        return {"message": "Tasks retrieved successfully!", "data": todos}

    else:
        todos = [
            {
                "_id": task._id,
                "title": task.title,
                "content": task.content,
                "priority": task.priority.value,
                "status": task.status.value,
                "dueDates": task.dueDates,
                "assignor": task.assignor,
                "assignee": task.assignee,
                "user_id": task.user_id,
                "dateCreated": task.dateCreated,
            }
            for task in Task.query.filter_by(assignee=username).all()
        ]
        return {"message": "Tasks retrieved successfully!", "data": todos}


# # Create New Task
@todos_bp.route("", methods=["POST"])
@authorized
def create_todo():
    data = request.get_json()
    schema = NewTaskSchema()

    try:
        schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    token = request.headers.get("Authorization").split(" ")[1]
    decode = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    user_id = decode["user_id"]
    username = decode["username"]

    todo = Task(
        title=data["title"],
        content=data["content"],
        priority=data["priority"],
        dueDates=data["dueDates"],
        assignor=username,
        assignee=data["assignee"],
        user_id=user_id,
        dateCreated=datetime.datetime.now(),
    )
    db.session.add(todo)
    db.session.commit()

    todo_dict = {
        "_id": todo._id,
        "title": todo.title,
        "content": todo.content,
        "priority": todo.priority.value,
        "dueDates": todo.dueDates,
        "assignor": todo.assignor,
        "assignee": todo.assignee,
        "user_id": todo.user_id,
        "dateCreated": todo.dateCreated,
    }

    return {"message": "Task created successfully!", "data": todo_dict}


# Delete Task
@todos_bp.route("/<int:_id>", methods=["DELETE"])
@authorized
def delete_todo(_id):
    token = request.headers.get("Authorization").split(" ")[1]
    decode = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    user_id = decode["user_id"]

    todo = Task.query.get(_id)

    if todo.user_id != user_id:
        return {"error": "Not authorized"}, 401

    if not todo:
        return {"error": "Task not found"}, 404

    db.session.delete(todo)
    db.session.commit()

    return {"message": "Task deleted successfully!"}


# Update Task
@todos_bp.route("/<int:_id>", methods=["PUT"])
@authorized
def update_todo(_id):
    data = request.get_json()

    todo = Task.query.get(_id)

    if not todo:
        return {"error": "Task not found"}, 404

    # Certain update
    title = data.get("title", todo.title)
    content = data.get("content", todo.content)
    priority = data.get("priority", todo.priority)
    status = data.get("status", todo.status)
    dueDates = data.get("dueDates", todo.dueDates)
    assignee = data.get("assignee", todo.assignee)
    assignor = data.get("assignor", todo.assignor)

    todo.title = title
    todo.content = content
    todo.priority = priority
    todo.status = status
    todo.dueDates = dueDates
    todo.assignee = assignee
    todo.assignor = assignor

    db.session.commit()

    todo_dict = {
        "_id": todo._id,
        "title": todo.title,
        "content": todo.content,
        "priority": todo.priority.value,
        "status": todo.status.value,
        "dueDates": todo.dueDates,
        "assignor": todo.assignor,
        "assignee": todo.assignee,
    }

    return {"message": "Task updated successfully!", "data": todo_dict}
