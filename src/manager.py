# Configurar o Gerenciador da Aplicação Flask
import os
from flask import Flask
from dotenv import load_dotenv
from extensions import db, login_manager, bcrypt

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "homepage"

from models import *
from routes import *

with app.app_context():
    db.create_all()
