# -*- coding: utf-8 -*-

from flask import request
from reddit.models.user import User
from reddit.app import app, datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response
from reddit.utils import error_message

import uuid
import json

def create_user(request_data):
	try:
		if not request_data.get('user_id', None):
			app.logger.error(error_message.USER_ID_MISSING)
			return bad_request(error_message.USER_ID_MISSING)

		user_id = request_data['user_id']

		if (datastore.users.get(user_id, None)):
			app.logger.error(error_message.ACCOUNT_ALREADY_EXISTS%user_id)
			return bad_request(error_message.ACCOUNT_ALREADY_EXISTS%user_id)

		user = User(user_id=user_id)

		datastore.users[user_id] = user
		return success_response(user)
	
	except Exception as e:
		app.logger.error(error_message.INTERNAL_ERROR)
		return internal_error(error_message.INTERNAL_ERROR)