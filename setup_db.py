from src import db, app, bcrypt
from src import models

with app.app_context():
    db.drop_all()
    db.create_all()
    password_hashed = bcrypt.generate_password_hash("123456").decode("utf-8")
    admin = models.user.User(username="toogni", password=password_hashed, role="admin")
    db.session.add(admin)
    db.session.commit()
    print("Database created!")
