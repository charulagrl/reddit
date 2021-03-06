# -*- coding: utf-8 -*-

from flask import request
from reddit.app import app, datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_dict_response
from reddit.utils import error_message

import uuid
import json

def create_upvote_json(request_data, topic_id):
	try:
		if not topic_id:
			app.logger.error(error_message.TOPIC_ID_MISSING)
			return bad_request(error_message.TOPIC_ID_MISSING)

		if not request_data.get('user_id', None):
			app.logger.error(error_message.USER_ID_MISSING)
			return bad_request(error_message.USER_ID_MISSING)

		topic = datastore.topics.get(topic_id, None)

		if not topic:
			app.logger.error(error_message.TOPIC_DOES_NOT_EXIST%topic_id)
			return not_found(error_message.TOPIC_DOES_NOT_EXIST%topic_id)

		user_id = request_data['user_id']
		if not datastore.users.get(user_id, None):
			app.logger.error(error_message.ACCOUNT_DOES_NOT_EXIST%user_id)
			return bad_request(error_message.ACCOUNT_DOES_NOT_EXIST%user_id)

		upvotes = datastore.upvotes.add_upvote(topic_id)
		return success_dict_response({"topic_id": topic_id, "upvotes": upvotes})

	except Exception as e:
		app.logger.error(error_message.INTERNAL_ERROR)
		return internal_error(error_message.INTERNAL_ERROR)

def create_upvote_html(topic_id):
	upvotes = datastore.upvotes.add_upvote(topic_id)
	return upvotes
