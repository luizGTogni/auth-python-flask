from src import app, db, models, bcrypt
from flask import request, jsonify
from flask_login import login_required, current_user

@app.route("/users/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    body = request.get_json()
    password = body.get("password")

    if password:
        user = models.user.User.query.get(user_id)
        
        if user:
            if user.id != current_user.id and current_user.role == "user":
                return jsonify({ "message": "You do not have permission for this operation" }), 403

            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
            db.session.commit()
            return jsonify(user.to_dict()), 200

        return jsonify({ "message": "User not found" }), 404
        
    return jsonify({ "message": "Data is missing or invalid" }), 400

