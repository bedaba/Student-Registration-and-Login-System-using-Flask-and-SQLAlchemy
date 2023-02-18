from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(
        'UserName',
        validators=[
                    DataRequired()
                    , Length(min=2, max=20)
                   ]
                 )
    email = StringField(
        'Email',
        validators=[
                    DataRequired(),
                    Length(min=2, max=100),
                    Email()
                   ]
                 )
    password = PasswordField(
        'passowrd',
        validators=[
                    DataRequired(),
                   ]
                 )
    confirmPassword = PasswordField(
        'Confirm Password',
        validators=[
                    DataRequired(),
                    EqualTo('password')
                   ]
                 )
    submit = SubmitField(
        'Sign Up',
                 )
class LoginForm(FlaskForm):
    username = StringField(
        'UserName',
        validators=[
                    DataRequired()
                    , Length(min=2, max=20)
                   ]
                 )
    password = PasswordField(
        'passowrd',
        validators=[
                    DataRequired(),
                   ]
                 )
    submit = SubmitField(
        'Submit',
                 )
class SubjectForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[
                    DataRequired()
                    , Length(min=2, max=20)
                   ]
                 )
    details = StringField(
        'Details',
        validators=[
                    DataRequired(),
                   ]
                 )
    title = StringField(
        'Title',
        validators=[
                    DataRequired()
                    , Length(min=2, max=20)
                   ]
                 )
    submit = SubmitField(
        'Submit',
                 )

