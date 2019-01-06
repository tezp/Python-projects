from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from flaskBlog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username : ', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email : ', validators=[DataRequired(), Email()])
    password = PasswordField('Password : ', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password : ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please try another username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken. Please try another email')


class LoginForm(FlaskForm):
    email = StringField('Email : ', validators=[DataRequired(), Email()])
    password = PasswordField('Password : ', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Update username : ', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Update email : ', validators=[DataRequired(), Email()])
    image = FileField('Upload profile pic :', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken. Please try another username')

    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already taken. Please try another email')


class RequestResetForm(FlaskForm):
    email = StringField('Enter email : ', validators=[DataRequired(), Email()])
    submit = SubmitField('Request for reset password')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No such email present. Please check again. ')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password : ', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password : ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset password')
