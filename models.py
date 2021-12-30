#models.py

# from enum import unique
# from sysTraining.app import home
from sysTraining import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(64),unique=True, index=True)
    username = db.Column(db.String(64),unique=True, index=True)
    password_hash = db.Column(db.String(255))
    
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
       
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Topic(db.Model):
    __tablename__ = 'topic'


    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    # header = db.Column(db.Text)
    content = db.Column(db.Text)


    def __init__(self,name,content):
        self.name = name
        self.content = content

    def __repr__(self):
        return f"topic name is {self.name}" 