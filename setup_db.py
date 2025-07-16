from src import db, app
from src.models.user import User

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database created!")