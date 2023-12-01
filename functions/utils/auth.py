from flask import request
import jwt, os
from functools import wraps
from auth.models import Role


def login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        authorization_header = request.headers.get("Authorization")
        if not authorization_header:
            return {"error": "Not authorized"}, 401

        token = authorization_header.split(" ")[1]

        try:
            decode = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            user_id = decode["user_id"]
            username = decode["username"]
            role = decode["role"]
            return func(user_id, username, role, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}, 401

        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401

    return wrapper


def authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization").split(" ")[1]
        try:
            decode = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            role = decode["role"]
            if role == Role.manager.value:
                return func(*args, **kwargs)
            else:
                return {"error": "Not authorized"}, 401

        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}, 401

        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401

    return wrapper


def update_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization").split(" ")[1]
        try:
            decode = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            role = decode["role"]
            if role == Role.manager.value or Role.employee.value:
                return func(*args, **kwargs)
            else:
                return {"error": "Not authorized"}, 401

        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}, 401

        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401

    return wrapper
