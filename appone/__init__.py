from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from appone.views import item_view

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)

