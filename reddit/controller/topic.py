# -*- coding: utf-8 -*-

from flask import request
from reddit.store import datastore
from reddit.app import app, datastore
from reddit.models.topic import Topic
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response, success_list_response
from reddit.utils import error_message

import uuid
import json

def create_topic(request_data):
	try:
		if not request_data.get('content', None):
			app.logger.error(error_message.CONTENT_MISSING)
			return bad_request(error_message.CONTENT_MISSING)

		if not request_data.get('user_id', None):
			app.logger.error(error_message.USER_ID_MISSING)
			return bad_request(error_message.USER_ID_MISSING)

		content = request_data['content']

		content_length = len(content)
		if content_length > 255:
			app.logger.error(error_message.CONTENT_LENGTH_EXCEEDED)
			return bad_request(error_message.CONTENT_LENGTH_EXCEEDED)

		user_id = request_data['user_id']
		if not datastore.users.get(user_id, None):
			app.logger.error(error_message.ACCOUNT_DOES_NOT_EXIST%user_id)
			return not_found(error_message.ACCOUNT_DOES_NOT_EXIST%user_id)

		new_id = str(uuid.uuid4())
		while (datastore.topics.get(new_id, None)):
			new_id = str(uuid.uuid4())

		topic = Topic(topic_id=new_id, content=content, user_id=user_id)

		datastore.topics[new_id] = topic

		return success_response(topic)
	except Exception as e:
		app.logger.error(error_message.INTERNAL_ERROR)
		return internal_error(error_message.INTERNAL_ERROR)

def get_topic(topic_id):
	topic = datastore.topics.get(topic_id, None)

	if not topic:
		return not_found(error_message.TOPIC_DOES_NOT_EXIST)

	return success_response(topic)

def get_all_topics():
	topics = [datastore.topics[topic].__dict__ for topic in datastore.topics.keys()]

	for topic in topics:
		topic["upvotes"] = datastore.upvotes[topic['id']].upvotes
		topic["downvotes"] = datastore.downvotes[topic['id']].downvotes

	return success_list_response(topics)

