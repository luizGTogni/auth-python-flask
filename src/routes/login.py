from flask import request, jsonify
from src import app, bcrypt
from src.models.user import User
from flask_login import login_user

@app.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    username = body.get("username")
    password_plain = body.get("password")

    if username and password_plain:
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password_plain):
            login_user(user)
            return jsonify({ "message": "Login Done" })

    return jsonify({ "message": "Credentials Invalid" }), 401
