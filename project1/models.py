from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    fullname = db.Column(db.String, nullable = False)
    username= db.Column(db.String, primary_key = True)
    password = db.Column(db.String, unique = True, nullable = False)

class Books(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key = True)
    author = db.Column(db.String, nullable = False)
    title = db.Column(db.String, nullable = False)
    year = db.Column(db.String, nullable = False)
