from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from sysTraining.models import User
# from flask_login import models

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


# #forms.py

# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# # from wtforms import validators
# from wtforms.validators import DataRequired, Email, EqualTo
# from wtforms import ValidationError

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     password = PasswordField('Password',validators=[DataRequired()])
#     submit = SubmitField("log in")


# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password',validators=[DataRequired(), EqualTo('pass_confirm','passwords must match')])
#     pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
#     submit = SubmitField('Register')•••••me=self.username.data).first():
#             raise ValidationError('Username has been registered')
   