import os
from flask import Flask, app, render_template,request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import flask_login
# from flask_login import LoginManager()

login_manager = flask_login.LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))


#need to consolodate to 1 function for each tab with parameters
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["SECRET_KEY"] = "secret!"
# app.config["fd"] = None
# app.config["child_pid"] = None
# socketio = SocketIO(app)


db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'
