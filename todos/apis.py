from flask import Blueprint, request
from todos.models import Task, NewTaskSchema
from marshmallow import ValidationError
from db import db
import jwt, os
from utils.bcrypt import bcrypt

todos_bp = Blueprint("todos", __name__)


# Get All Tasks
@todos_bp.route("", methods=["GET"])
# ADD AUTH
# ADD IF MANAGER CAN SEE ALL TASKS, IF EMPLOYEE CAN SEE ONLY THOSE TASKS ASSIGNED TO HIM
def get_todos():
    todos = Task.query.all()
    return {"data": todos}
