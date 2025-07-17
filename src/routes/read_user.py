from src import app, models
from flask import jsonify
from flask_login import login_required, current_user

@app.route("/users/<int:user_id>", methods=["GET"])
@login_required
def read_user(user_id):
    user = models.user.User.query.get(user_id)

    if user:
        if user.id != current_user.id and current_user.role == "user":
            return jsonify({ "message": "You do not have permission for this operation" }), 403

        return jsonify(user.to_dict()), 200
    
    return jsonify({ "message": "User not found" }), 404