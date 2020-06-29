from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField
import config
class Upload(FlaskForm):
    name = StringField('NAME', validators=[DataRequired()])
    second_name = StringField('second_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()] )
    file = FileField('txt', validators=[
        FileRequired(),
        FileAllowed(['txt'], '.txt file only!')
    ])         
    submit = SubmitField('Загрузить')