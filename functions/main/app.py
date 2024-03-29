import os
from flask import Flask
from db import db, db_init
from auth.apis import auth_bp
from todos.apis import todos_bp
from flask_cors import CORS
from flask_talisman import Talisman
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

CORS(app, resources={r"/*": {"origins": "*"}})
Talisman(app)

database_url = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
print(database_url)
db.init_app(app)


# Home
@app.route("/")
def index():
    return "Week 22 Rayhan Zou"


# Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/users")
app.register_blueprint(todos_bp, url_prefix="/api/todos")


# # Database Migration
# with app.app_context():
#     db_init()
