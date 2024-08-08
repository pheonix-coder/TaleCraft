from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User: {self.username}>"

    @property
    def id(self):
        return self.uid

class Story(db.Model):
    __tablename__ = "stories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    story = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref=db.backref('stories', lazy=True))

    def __repr__(self):
        return f"<Story: {self.title}>"
