from flask_sqlalchemy import SQLAlchemy
from appone import app


db=SQLAlchemy(app)

class Registertable(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(40), unique=True, nullable=False)
    email=db.Column(db.String(40), unique=True, nullable=False)
    position=db.Column(db.String(40) ,nullable=False)
