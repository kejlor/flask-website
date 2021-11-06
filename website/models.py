from sqlalchemy.sql import func

from . import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    todos = db.relationship('Todo')
