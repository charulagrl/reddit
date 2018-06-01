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
from flask import request

import uuid
import json

def create_user_html(form):
	'''Create user when Accept type is text/html'''
	user_id = form.user_id.data
	user = User(user_id=user_id)
	datastore.users[user_id] = user
	return user

def create_user(request):
	'''Create user when Accept type is application/json'''
	try:
		if not request.json.get('user_id', None):
			app.logger.error(error_message.USER_ID_MISSING)
			return bad_request(error_message.USER_ID_MISSING)

		user_id = request.json['user_id']

		if (datastore.users.get(user_id, None)):
			app.logger.error(error_message.ACCOUNT_ALREADY_EXISTS%user_id)
			return bad_request(error_message.ACCOUNT_ALREADY_EXISTS%user_id)

		user = User(user_id=user_id)

		datastore.users[user_id] = user
		return success_response(user)
	
	except Exception as e:
		app.logger.error(error_message.INTERNAL_ERROR)
		return internal_error(error_message.INTERNAL_ERROR)
