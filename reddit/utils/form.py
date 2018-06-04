# -*- coding: utf-8 -*-

from wtforms import Form, TextField, BooleanField, PasswordField, TextAreaField, validators, SubmitField
from reddit.app import datastore
from reddit.utils import error_message
from wtforms.validators import ValidationError



class UserForm(Form):
	user_id= TextField('user_id', validators=[validators.Required(), validators.Length(min=4, max=25)])

	def validate_user_id(form, field):
		if datastore.users.get(form.user_id.data, None):
			raise ValidationError(error_message.ACCOUNT_ALREADY_EXISTS%form.user_id.data)

class TopicForm(Form):
	content = TextField('content', validators=[validators.Required(), validators.Length(min=4, max=255)])

class LoginForm(Form):
	user_id= TextField('user_id', validators=[validators.Required(), validators.Length(min=4, max=25)])

	def validate_user_id(form, field):
		if not datastore.users.get(form.user_id.data, None):
			raise ValidationError(error_message.ACCOUNT_DOES_NOT_EXIST%form.user_id.data)
