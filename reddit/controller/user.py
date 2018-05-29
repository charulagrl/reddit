# -*- coding: utf-8 -*-

from flask import request, Response
from reddit.store import datastore
from reddit.models.user import User
from reddit.app import app, datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response

import uuid
import json

def create_user(request_data):
	try:
		if not request_data.get('user_id', None):
			app.logger.error("User_id is missing")
			return bad_request("User_id is missing")

		user_id = request_data['user_id']

		if (datastore.users.get(user_id, None)):
			return bad_request("Account with user id %s already exists"%user_id)

		user = User(user_id=user_id)

		datastore.users[user_id] = user
		return success_response(user)
	
	except Exception as e:
		app.logger.error("Some unexpected error has occured.")
		return internal_error("Some unexpected error has occured.")