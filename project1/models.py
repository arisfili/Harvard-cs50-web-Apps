from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    fullname = db.Column(db.String, nullable = False)
    username= db.Column(db.String, primary_key = True)
    password = db.Column(db.String, unique = True, nullable = False)

