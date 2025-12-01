from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


def validate_password(form, field):
    import re
    password = field.data
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&]).{8,12}$"
    
    if not re.match(pattern, password):
        raise ValidationError('Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)')

class RecipeForm(FlaskForm):
    cook_time = IntegerField('Cook Time',
        validators=[DataRequired(), NumberRange(min=1, max=60*24*7)])
    description = StringField('Description', validators=[DataRequired()])
    intro = StringField('Intro', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time',
        validators=[DataRequired(), NumberRange(min=1, max=60*24*7)])
    servings = IntegerField('Servings',
        validators=[DataRequired(), NumberRange(min=1, max=10000)])
    submit = SubmitField('Create')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), validate_password])
    submit = SubmitField('Register')
