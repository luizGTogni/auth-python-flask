from src import app, bcrypt, models, db
from flask import request, jsonify

@app.route("/users", methods=["POST"])
def create_user():
    body = request.get_json()
    username = body.get("username")
    password = body.get("password")

    if username and password:
        has_user = models.user.User.query.filter_by(username=username).first()

        if not has_user:
            password_hashed = bcrypt.generate_password_hash(password).decode("utf-8")
            user_created = models.user.User(username=username, password=password_hashed, role="user")

            db.session.add(user_created)
            db.session.commit()

            return jsonify({ "message": "Created user successfully", "id": user_created.id }), 201
        
        return jsonify({ "message": "User already exists" }), 400

    return jsonify({ "message": "Data is missing or invalid" }), 400