from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flasktodo.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[ DataRequired(),Length(min=3, max=25)])
    email = StringField('Email',  
                        validators=[DataRequired(), Email()])
    password= PasswordField('Password',
                        validators=[DataRequired(),] )
    confirm_password= PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')] )
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self,email):
        user = User.query.filter_by(email =email.data).first()
        if user:
            raise ValidationError('Email is taken, please try another one')


class LoginForm(FlaskForm):
    email = StringField('Email',  
                        validators=[DataRequired(), Email()])
    password= PasswordField('Password',
                        validators=[DataRequired(),] )
    remember = BooleanField ('Remember me')
    submit = SubmitField('Login')



class AccountUpdate(FlaskForm):
    username = StringField('Username',
                        validators=[ DataRequired(),Length(min=3, max=25)])
    email = StringField('Email',  
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile picutre', validators= [FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update account information')

    def validate_username(self, username):
        if username.data!=  current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

    def validate_email(self,email):
        if email.data!=  current_user.email:
            user = User.query.filter_by(email =email.data).first()
            if user:
                raise ValidationError('Email is taken, please try another one')
