from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class registraion_form(FlaskForm):
    username=StringField('User Name',validators=[DataRequired(),Length(min=2,max=10)])
    email=StringField('Email address',validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    Confirm_pwd=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class login_form(FlaskForm):
    email=StringField('Email address',validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember=BooleanField('Remeber Me')
    submit=SubmitField('Login Up')