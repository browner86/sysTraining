# import os
# from
# from flask import Flask, app, render_template,request

# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from flask_migrate import Migrate




# basedir = os.path.abspath(os.path.dirname(__file__))


# #need to consolodate to 1 function for each tab with parameters
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# from werkzeug import datastructures
from sysTraining import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from sysTraining.models import User
from sysTraining.forms import LoginForm, RegistrationForm
# from flask_socketio import SocketIO
# import pty
# import os
# import subprocess
# import select
# import termios
# import struct
# import fcntl
# import shlex
##############
### MODELS ###
##############

#initialize the database
# db = SQLAlchemy(app)
# Migrate(app,db)

#create db model
# class Topic(db.Model):
#     __tablename__ = 'topic'


#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.Text)
#     # header = db.Column(db.Text)
#     content = db.Column(db.Text)


#     def __init__(self,name,content):
#         self.name = name
#         self.content = content

#     def __repr__(self):
#         return f"topic name is {self.name}" 

      



##################################
####### VIEW FUNCTIONS ###########
##################################

@app.route('/')
def home():
    name = "Home"
    training_list = ["Training"]
    title = f"{name} | SYS Training"
    return render_template('home.html',title=title, name=name, training_list=training_list)

@app.route('/welcome_user')
# @login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You Logged out.")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)

# @app.route('/login', methods =['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()

#         if user.check_password(form.password.data) and user is not None:

#             login_user(user)
#             flash('Logged in Successfully!')

#             next = request.args.get('next')

#             if next == None or not next[0]=='/':
#                 next = url_for('welcome_user')

#             return redirect(next)
        
#     return render_template('login.html',form=form)


@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.username.data
                    )
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/training')
def training(topic):
    name = topic
    training_list = ["Training"]
    title = f"{name} | SYS Training"
    return render_template('index.html',title=title, name=name, training_list=training_list)

@app.route('/linux')
def linux():
    name= "Linux"
    training_list = ["Cron"
                    , 'Commands'
                    , 'Patching'
                    , 'Auto-Mounting'
                    , 'Scripts'
                    , 'Password'
                    , 'Vim'
                    , 'Security'
                    , 'Bash'
                    , 'SH'
                    , 'KSH'
                    , 'CSH'
                    , 'Boot-up'
                    , 'systemd']

    title = f"{name} | SYS Training"
    return render_template("linux.html", title=title, name=name, training_list=training_list )

@app.route('/windows')
def windows():
    name= "Windows"
    training_list = ["CMD", 'Cheat Sheet', 'Updates']
    title = f"{name} | SYS Training"
    return render_template("windows.html", title=title, name=name, training_list=training_list)

@app.route('/cheatsheet')
def cheatsheet():
    name= "Cheatsheet"
    training_list = ["Cron"
                    , 'Commands'
                    , 'Patching'
                    , 'Auto-Mounting'
                    , 'Centrify'
                    , 'Scripts'
                    , 'Password'
                    , 'Vim'
                    , 'Security'
                    , 'Bash'
                    , 'SH'
                    , 'KSH'
                    , 'CSH'
                    , 'Boot-up'
                    , 'systemd']

    title = f"{name} | SYS Training"
    return render_template("cheatsheet.html", title=title, name=name, training_list=training_list )

@app.route('/videos')
def videos():
    name= "Videos"
    training_list = ["Cron"
                    , 'Commands'
                    , 'Patching'
                    , 'Auto-Mounting'
                    , 'Centrify'
                    , 'Scripts'
                    , 'Password'
                    , 'Vim'
                    , 'Security'
                    , 'Bash'
                    , 'SH'
                    , 'KSH'
                    , 'CSH'
                    , 'Boot-up'
                    , 'systemd']

    title = f"{name} | SYS Training"
    return render_template("videos.html", title=title, name=name, training_list=training_list )
    

@app.route('/tasks')
def tasks():
    name= "Tasks"
    training_list = ["Cron"
                    , 'Commands'
                    , 'Patching'
                    , 'Auto-Mounting'
                    , 'Centrify'
                    , 'Scripts'
                    , 'Password'
                    , 'Vim'
                    , 'Security'
                    , 'Bash'
                    , 'SH'
                    , 'KSH'
                    , 'CSH'
                    , 'Boot-up'
                    , 'systemd']

    title = f"{name} | SYS Training"
    return render_template("tasks.html", title=title, name=name, training_list=training_list )


@app.route('/admin')
def admin():
    name= "Admin"
    title = f"{name} | SYS Training"
    return render_template("admin.html", title=title, name=name )


# @app.route('/signIn')
# def signIn():
#     name= "Sign In"
#     title = f"{name} | SYS Training"
#     return render_template("login.html", title=title, name=name )

# @app.route('/registeration', methods=['POST', 'GET'])
# def registeration():
#     name= "Registration"
#     title = f"{name} | SYS Training"
#     # if request.method == "POST"
#     return render_template("registeration.html", title=title, name=name )

# @app.route('/registerUser')
# def registerUser():
#     name= "Registration"
#     title = f"{name} | SYS Training"
#     return render_template("registrationSuccess.html", title=title, name=name )


@app.route('/basic_commands')
def basic_commands():
    name= "Basic Commands"
    title = f"{name} | SYS Training"
    return render_template("basic_commands.html", title=title, name=name )

@app.route('/file_permissions')
def file_permissions():
    name= "Basic Commands"
    title = f"{name} | SYS Training"
    return render_template("file_permissions.html", title=title, name=name )


if __name__ == '__main__':
    app.run(debug=True)