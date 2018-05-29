# -*- coding: utf-8 -*-

from flask import request, Response
from reddit.store import datastore
from reddit.models.topic import Topic
from reddit.models.upvote import Upvote
from reddit.models.downvote import Downvote
from reddit.app import app, datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response, success_list_response

import uuid
import json

def create_topic(request_data):
	try:
		if not request_data.get('content', None):
			app.logger.error("Content is missing")
			return bad_request("Content is missing")

		content = request_data['content']

		content_length = len(content)
		if content_length > 255:
			app.logger.error("Content length is longer than 255 characters")
			return bad_request("Content length is longer than 255 characters")

		new_id = str(uuid.uuid4())
		while (datastore.topics.get(new_id, None)):
			new_id = str(uuid.uuid4())

		topic = Topic(topic_id=new_id, content=content)
		upvote = Upvote(topic_id=new_id)
		downvote = Downvote(topic_id=new_id)

		datastore.topics[new_id] = topic
		datastore.upvotes[new_id] = upvote
		datastore.downvotes[new_id] = downvote

		return success_response(topic)
	except Exception as e:
		app.logger.error("Some unexpected error has occured.")
		return internal_error("Some unexpected error has occured.")

def get_topic(topic_id):
	topic = datastore.topics.get(topic_id, None)

	if not topic:
		return not_found("Topic with id %s does not exist"%topic_id)

	return success_response(topic)

def get_all_topics():
	topics = [datastore.topics[topic].__dict__ for topic in datastore.topics.keys()]

	for topic in topics:
		topic["upvotes"] = datastore.upvotes[topic['id']].upvotes
		topic["downvotes"] = datastore.downvotes[topic['id']].downvotes

	return success_list_response(topics)

