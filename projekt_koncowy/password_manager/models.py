from flask_login import UserMixin
from password_manager import db, login_manager
from sqlalchemy.types import TypeDecorator, String
import json

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    created_records= db.relationship('Login_Record', backref='owner', lazy=True)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class PasswordRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



