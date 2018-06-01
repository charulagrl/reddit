# -*- coding: utf-8 -*-

from wtforms import Form, TextField, BooleanField, PasswordField, TextAreaField, validators, SubmitField
from reddit.app import datastore
from wtforms.validators import ValidationError



class UserForm(Form):
    user_id= TextField('user_id', validators=[validators.Required(), validators.Length(min=4, max=25)])

class TopicForm(Form):
	content = TextField('content', validators=[validators.Required(), validators.Length(min=4, max=255)])
	user_id= TextField('user_id', validators=[validators.Required(), validators.Length(min=4, max=25)])

	def validate_user_id(form, field):
		if not datastore.users.get(form.user_id.data, None):
			raise ValidationError('Account does not exist for user_id %s'%form.user_id.data)