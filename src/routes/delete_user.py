from src import app, models, db
from flask import jsonify
from flask_login import login_required, current_user, logout_user

@app.route("/users/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = models.user.User.query.get(user_id)
    if user:
        if user.id == current_user.id:
            return jsonify({ "message": "You are not allowed to delete this user" }), 403
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({ "message": "User deleted successfully" }), 200
    
    return jsonify({ "message": "User not found" }), 404