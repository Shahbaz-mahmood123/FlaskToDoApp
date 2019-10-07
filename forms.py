from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[ DataRequired(),Length(min=3, max=25)])

    firstname= StringField ('First Name', validators=[DataRequired()])

    surname = StringField('Surname', validators=[DataRequired])

    email = StringField('Email',  
                        validators=[DataRequired(), Email()])
    password= PasswordField('Password',
                        validators=[DataRequired(),] )
    confirm_password= PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')] )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',  
                        validators=[DataRequired(), Email()])
    password= PasswordField('Password',
                        validators=[DataRequired(),] )
    remember = BooleanField ('Remember me')
    submit = SubmitField('Login')