
from flask import Flask, render_template,Response, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from io import BytesIO
from werkzeug.utils import secure_filename
from pytz import timezone
from flask_login import UserMixin
from datetime import datetime
from . import db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    workouts = db.relationship('Workout', backref='author', lazy=True)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, nullable=False,default=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
