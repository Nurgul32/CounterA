from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField
import config
from flask_sqlalchemy import SQLAlchemy
from app import app
#db = SQLAlchemy(app)
#class Message(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #text=db.Column(db.String(1024), nullable=False)
#class Tag(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #text=db.Column(db.String(32), nullable=False)
    #message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    #message = db.relationship('Message', backref=db.backref('tags', lazy=True))

#db.create_all()
class Upload(FlaskForm):
    name = StringField('NAME', validators=[DataRequired()])
    second_name = StringField('second_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()] )
    file = FileField('txt', validators=[
        FileRequired(),
        FileAllowed(['txt'], '.txt file only!')
    ])         
    submit = SubmitField('Загрузить')