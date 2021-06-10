from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from password_manager.config import Config


app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(Config)

login_manager = LoginManager(app)

from password_manager import routes