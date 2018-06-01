# -*- coding: utf-8 -*-

from wtforms import Form, TextField, BooleanField, PasswordField, TextAreaField, validators, SubmitField
from reddit.models.user import User

class UserForm(Form):
    user_id= TextField('user_id', validators=[validators.Required(), validators.Length(min=4, max=25)])
