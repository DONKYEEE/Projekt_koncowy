from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, UsernameField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
     email = StringField('Email', validators=[DataRequired(), Email()])
     password = PasswordField('Password', validators=[DataRequired()])
     confirm_password = PasswordField('Confirm password',validators=[DataRequired(), EqualTo('password')])
     sumbit = SubmitField('Submit')

class PasswordRecord(FlaskForm):
    username = UsernameField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    