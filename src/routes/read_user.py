from src import app, models
from flask import jsonify
from flask_login import login_required

@app.route("/users/<int:user_id>", methods=["GET"])
@login_required
def read_user(user_id):
    user = models.user.User.query.get(user_id)

    if user:
        return jsonify(user.to_dict()), 200
    
    return jsonify({ "message": "User not found" }), 404