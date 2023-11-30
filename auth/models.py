from db import db
from marshmallow import Schema, fields, validate
from enum import Enum
from sqlalchemy import Enum as EnumType


class Role(Enum):
    manager = "manager"
    employee = "employee"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(EnumType(Role), default=Role.employee, nullable=False)


class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserRegisterSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(
        required=True, validate=validate.Regexp(r"^(?=.*[a-zA-Z])(?=.*\d)")
    )
    # role = fields.Str(required=True, validate=validate.OneOf(Role))
    role = fields.Str(
        required=True, validate=validate.OneOf([role.value for role in Role])
    )
