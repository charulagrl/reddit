# -*- coding: utf-8 -*-

from reddit.utils.request_type import request_wants_html
from reddit.models.user import User
from reddit.app import app, datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response
from reddit.utils import error_message
from reddit.utils.form import UserForm
from reddit.utils import current_user
from flask import request

import uuid
import json

def create_user_internal(user_id):
	'''Creates new user object given user_id'''
	user = User(user_id=user_id)
	datastore.users[user_id] = user
	current_user.set_current_user(user)
	return user

def create_user_html(form):
	'''Creates user when Accept type is text/html'''
	user_id = form.user_id.data
	user = create_user_internal(user_id)
	return user

def create_user_json(request):
	'''Creates user when Accept type is application/json'''
	try:
		if not request.json.get('user_id', None):
			app.logger.error(error_message.USER_ID_MISSING)
			return bad_request(error_message.USER_ID_MISSING)

		user_id = request.json['user_id']

		if (datastore.users.get(user_id, None)):
			app.logger.error(error_message.ACCOUNT_ALREADY_EXISTS%user_id)
			return bad_request(error_message.ACCOUNT_ALREADY_EXISTS%user_id)

		user = create_user_internal(user_id)
		return success_response(user)
	
	except Exception as e:
		app.logger.error(error_message.INTERNAL_ERROR)
		return internal_error(error_message.INTERNAL_ERROR)

def user_login(form):
	user_id = form.user_id.data
	user = datastore.get_user(user_id)
	current_user.set_current_user(user)

def user_logout():
	current_user.unset_current_user()
