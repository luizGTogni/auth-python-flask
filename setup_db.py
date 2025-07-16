from src import db, app, bcrypt
from src import models

with app.app_context():
    db.drop_all()
    db.create_all()
    admin = models.user.User(username="admin", password=bcrypt.generate_password_hash("123456").decode("utf-8"))
    db.session.add(admin)
    db.session.commit()
    print("Database created!")