from flask import Blueprint, request
from auth.models import User, UserRegisterSchema, UserLoginSchema
from marshmallow import ValidationError
from db import db
import jwt, os, datetime
from utils.bcrypt import bcrypt


auth_bp = Blueprint("auth", __name__)


# Register User
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    schema = UserRegisterSchema()

    try:
        schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    if User.query.filter_by(username=data["username"]).first():
        return {"error": "Username already exists"}, 400

    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role=data["role"],
    )
    db.session.add(user)
    db.session.commit()

    return {
        "message": "User registered successfully!",
        "data": {"email": user.email, "username": user.username},
    }


# Login User
@auth_bp.route("/login", methods=["POST"])
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
        "role": user.role.value,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=5),
    }

    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm="HS256")

    return {"message": "Logged in successfully!", "data": token}
