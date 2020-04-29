from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class RegistrationForm(FlaskForm):
    fullname = StringField("fullname", validators=[DataRequired(),
                                                   Length(min=5, max=25)])
    username = StringField("username", validators=[DataRequired(),
                                                   Length(min=5, max=25)])
    password = PasswordField("password", validators=[DataRequired()])

    confirm_password = PasswordField("confirm password", validators=[DataRequired(), equal_to("password")])

    submit = SubmitField("Sign up")

class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
