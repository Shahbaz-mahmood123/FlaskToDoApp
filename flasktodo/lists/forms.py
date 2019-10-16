from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ListForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content= TextAreaField('List Details', validators=[DataRequired()])
    submit = SubmitField('Create new list')