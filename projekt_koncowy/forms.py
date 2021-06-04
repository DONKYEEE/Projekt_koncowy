from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
bcrypt = Bcrypt()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Email()])
     password = PasswordField('Password', validators=[DataRequired()])
     confirm_password = PasswordField('Confirm password',validators=[DataRequired(), EqualTo('password')])
     sumbit = SubmitField('Submit')
    

    