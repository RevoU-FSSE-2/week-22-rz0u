from datetime import datetime
from main.db import db
from marshmallow import Schema, fields
from enum import Enum
from sqlalchemy import Enum as EnumType


class Priority(Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Status(Enum):
    completed = "completed"
    todo = "To Do"
    ongoing = "ongoing"


class Task(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    priority = db.Column(EnumType(Priority), default=Priority.medium, nullable=False)
    status = db.Column(EnumType(Status), default=Status.todo, nullable=False)
    dueDates = db.Column(db.DateTime, nullable=False)
    assignor = db.Column(db.String(50), nullable=False)
    assignee = db.Column(db.String(50), nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user._id"), nullable=False)
    user = db.relationship("User", backref=db.backref("tasks", lazy=True))


class NewTaskSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    priority = fields.Str(required=True)
    dueDates = fields.Str(required=True)
    assignee = fields.Str(required=True)
