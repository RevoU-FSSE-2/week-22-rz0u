import os, jwt, datetime
from flask import Flask, request
from db import db, db_init
from marshmallow import Schema, fields, ValidationError, validate
from enum import Enum
from sqlalchemy import Enum as EnumType
from flask_bcrypt import Bcrypt
from auth.apis import auth_bp

app = Flask(__name__)

database_url = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
print(database_url)
db.init_app(app)

bcrypt = Bcrypt(app)


# Home
@app.route("/")
def index():
    return "Week 22 Rayhan Zou"


# Blueprints
app.register_blueprint(auth_bp, url_prefix="/users")


# Class
# class Role(Enum):
#     manager = "manager"
#     employee = "employee"


# class User(db.Model):
#     _id: db.Column(db.Integer, primary_key=True)
#     username: db.Column(db.String(50), unique=True, nullable=False)
#     email: db.Column(db.String(50), unique=True, nullable=False)
#     password: db.Column(db.String(100), nullable=False)
#     role: db.Column(EnumType(Role), default=Role.employee, nullable=False)


# class Priority(Enum):
#     high = "high"
#     medium = "medium"
#     low = "low"


# class Status(Enum):
#     completed = "completed"
#     todo = "To Do"
#     ongoing = "ongoing"


# class Task(db.Model):
#     _id: db.Column(db.Integer, primary_key=True)
#     title: db.Column(db.String(50), nullable=False)
#     content: db.Column(db.String(100), nullable=False)
#     priority: db.Column(EnumType(Priority), default=Priority.medium, nullable=False)
#     status: db.Column(EnumType(Status), default=Status.todo, nullable=False)
#     dueDates: db.Column(db.DateTime, nullable=False)
#     assignor: db.Column(db.String(50), nullable=False)
#     assignee: db.Column(db.String(50), nullable=False)
#     dateCreated: db.Column(db.DateTime.now, default=datetime.now(), nullable=False)
#     user_id: db.Column(db.Integer, db.ForeignKey("user._id"), nullable=False)
#     user: db.relationship("User", backref=db.backref("tasks", lazy=True))


# class UserLoginSchema(Schema):
#     username = fields.Str(required=True)
#     password = fields.Str(required=True)


# class UserRegisterSchema(Schema):
#     username = fields.Str(required=True)
#     email = fields.Email(required=True)
#     password = fields.Str(
#         required=True, validate=validate.Regexp(r"^(?=.*[a-zA-Z])(?=.*\d)")
#     )
#     role = fields.Str(required=True, validate=validate.OneOf(Role))
#     # role = fields.Str(required=True, validate=validate.OneOf([role.value for role in Role]))


# # Register User
# @app.route("/api/v1/users/register", methods=["POST"])
# def register():
#     data = request.get_json()
#     schema = UserRegisterSchema()

#     try:
#         schema.load(data)
#     except ValidationError as err:
#         return {"error": err.messages}, 400

#     if User.query.filter_by(username=data["username"]).first():
#         return {"error": "Username already exists"}, 400

#     hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
#     user = User(username=data["username"], password=hashed_password, role=data["role"])
#     db.session.add(user)
#     db.session.commit()

#     return {
#         "message": "User registered successfully!",
#         "data": {"email": user.email, "username": user.username},
#     }


# # Login User
# @app.route("/api/v1/users/login", methods=["POST"])
# def login():
#     data = request.get_json()
#     schema = UserLoginSchema()

#     try:
#         schema.load(data)
#     except ValidationError as err:
#         return {"error": err.messages}, 400

#     user = User.query.filter_by(username=data["username"]).first()
#     if not user or not bcrypt.check_password_hash(user.password, data["password"]):
#         return {"error": "Invalid username or password"}, 401

#     payload = {
#         "user_id": user._id,
#         "username": user.username,
#         "role": user.role,
#     }

#     token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")

#     return {"message": "Logged in successfully!", "data": token}


# # Get All Tasks
# @app.route("/api/v1/todos", methods=["GET"])
# # ADD AUTH
# # ADD IF MANAGER CAN SEE ALL TASKS, IF EMPLOYEE CAN SEE ONLY THOSE TASKS ASSIGNED TO HIM
# def get_todos():
#     todos = Task.query.all()
#     return {"data": todos}


# # Create New Task
# @app.route("/api/v1/todos", methods=["POST"])
# # ADD AUTH
# # ADD ONLY MANAGER CAN CREATE TASKS
# def create_todo():
#     data = request.get_json()
#     todo = Task(
#         title=data["title"],
#         content=data["content"],
#         priority=data["priority"],
#         status=data["status"],
#         dueDates=data["dueDates"],
#         assignor=data["assignor"],
#         assignee=data["assignee"],
#     )
#     db.session.add(todo)
#     db.session.commit()
#     return {"message": "Task created successfully!", "data": todo}


# # Delete Task
# @app.route("/api/v1/todos/<int:_id>", methods=["DELETE"])
# # ADD AUTH
# # ADD ONLY MANAGER CAN DELETE TASKS
# def delete_todo(_id):
#     todo = Task.query.get(_id)
#     if not todo:
#         return {"error": "Task not found"}, 404
#     db.session.delete(todo)
#     db.session.commit()
#     return {"message": "Task deleted successfully!"}


# # Update Task
# @app.route("/api/v1/todos/<int:_id>", methods=["PUT"])
# # ADD AUTH
# def update_todo(_id):
#     data = request.get_json()
#     todo = Task.query.get(_id)
#     if not todo:
#         return {"error": "Task not found"}, 404
#     todo.title = data["title"]
#     todo.content = data["content"]
#     todo.priority = data["priority"]
#     todo.status = data["status"]
#     todo.dueDates = data["dueDates"]
#     todo.assignor = data["assignor"]
#     todo.assignee = data["assignee"]
#     db.session.commit()
#     return {"message": "Task updated successfully!", "data": todo}


# # Database Migration
# with app.app_context():
#     db_init()

# # ROUTE WITH ID
# @app.route('/api/todos/<int:todo_id>')
# def get_todo(todo_id):
#    # todo_id variable will contain the id path segment
#    return {'id': todo_id}
