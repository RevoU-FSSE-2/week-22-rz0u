import os, jwt, datetime
from flask import Flask, request
from db import db, db_init
from marshmallow import Schema, fields, ValidationError, validate
from enum import Enum
from sqlalchemy.orm import Enum as EnumType
from flask_bcrypt import Bcrypt

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
print(database_url)
db.init_app(app)

bcrypt = Bcrypt(app)


# Home
@app.route("/")
def index():
    return "Week 22 Rayhan Zou"


# Blueprints


# Class
class Role(Enum):
    manager = "manager"
    employee = "employee"


class User(db.Model):
    _id: db.Column(db.Integer, primary_key=True)
    username: db.Column(db.String(50), unique=True, nullable=False)
    password: db.Column(db.String(100), nullable=False)
    role: db.Column(EnumType(Role), default=Role.employee, nullable=False)


class Priority(Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Status(Enum):
    completed = "completed"
    todo = "To Do"
    ongoing = "ongoing"


class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserRegisterSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(
        required=True, validate=validate.Regexp(r"^(?=.*[a-zA-Z])(?=.*\d)")
    )
    role = fields.Str(required=True, validate=validate.OneOf(Role))
    # role = fields.Str(required=True, validate=validate.OneOf([role.value for role in Role]))


class Task(db.Model):
    _id: db.Column(db.Integer, primary_key=True)
    title: db.Column(db.String(50), nullable=False)
    content: db.Column(db.String(100), nullable=False)
    priority: db.Column(EnumType(Priority), default=Priority.medium, nullable=False)
    status: db.Column(EnumType(Status), default=Status.todo, nullable=False)
    dueDates: db.Column(db.DateTime, nullable=False)
    assignor: db.Column(db.String(50), nullable=False)
    assignee: db.Column(db.String(50), nullable=False)
    dateCreated: db.Column(db.DateTime.now, default=datetime.now(), nullable=False)
    user_id: db.Column(db.Integer, db.ForeignKey("user._id"), nullable=False)


@app.route("/api/v1/users/login", methods=["POST"])
def login():
    data = request.get_json()
    schema = UserLoginSchema()

    try:
        schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    user = User.query.filter_by(username=data["username"]).first()
    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return {"error": "Invalid username or password"}, 401

    payload = {
        "user_id": user._id,
        "username": user.username,
        "role": user.role,
    }

    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

    return {"message": "Logged in successfully!", "data": token}


# # Database Migration
# with app.app_context():
#     db_init()
