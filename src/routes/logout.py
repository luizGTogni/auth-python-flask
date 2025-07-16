from src import app
from flask import jsonify
from flask_login import logout_user, login_required

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({ "message": "Successfully logged out" })
