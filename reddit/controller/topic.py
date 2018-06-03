# -*- coding: utf-8 -*-
from reddit.utils.success import success_response, success_list_response
from reddit.utils.errors import internal_error, not_found, bad_request
from reddit.utils.request_type import request_wants_html
from reddit.app import app, datastore
from reddit.models.topic import Topic
from reddit.utils import error_message
from flask import request

import uuid
import json

def create_topic_internal(topic_id, user_id, content):
	'''Creates new topic object given user_id, topic_id, content'''
	topic = Topic(topic_id=topic_id, content=content, user_id=user_id)

	datastore.topics[topic_id] = topic
	datastore.upvotes.create_upvote(topic_id)
	datastore.downvotes.create_downvote(topic_id)
	return topic

def create_topic_json(request_data):
	'''Creates topic when Accept type is application/json'''
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

		topic = create_topic_internal(new_id, user_id, content)
		return success_response(topic)

	except Exception as e:
		app.logger.error(error_message.INTERNAL_ERROR)
		return internal_error(error_message.INTERNAL_ERROR)

def create_topic_html(form):
	'''Creates topic when Accept type is text/html'''
	content = form.content.data
	user_id = datastore.current_user.user_id
		
	new_id = str(uuid.uuid4())
	while (datastore.topics.get(new_id, None)):
		new_id = str(uuid.uuid4())

	topic = create_topic_internal(new_id, user_id, content)
	return topic

def get_topic(topic_id):
	'''Get topic by topic_id'''
	topic = datastore.get_topic(topic_id)
	if request_wants_html():
		return topic
	else:
		if not topic:
			return not_found(error_message.TOPIC_DOES_NOT_EXIST)

		return success_response(topic)

def get_all_topics():
	'''Return all the topics'''
	topics = datastore.get_all_topics()

	if request_wants_html():
		return topics
	else:
		return success_list_response(topics)
