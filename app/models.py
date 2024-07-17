from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    published_date = db.Column(db.String(20), nullable=False)
    isbn = db.Column(db.String(20), nullable=False, unique=True)
