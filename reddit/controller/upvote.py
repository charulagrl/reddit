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
from reddit.utils.success import success_response

import uuid
import json

def create_upvote(request_data):
	try:
		if not request_data.get('topic_id', None):
			app.logger.errors("Topic id is missing")
			return bad_request("Topic id is missing")

		if not request_data.get('user_id', None):
			app.logger.error("User id is missing")
			return bad_request("User id is missing")

		topic_id = request_data['topic_id']
		topic = datastore.topics.get(topic_id, None)

		if not topic:
			app.logger.error("Topic with id %s does not exist"%topic_id)
			return not_found("Topic with id %s does not exist"%topic_id)

		user_id = request_data['user_id']
		if not datastore.users.get(user_id, None):
			app.logger.error("Account with user_id %s does not exist"%user_id)
			return bad_request("Account with user_id %s does not exist"%user_id)

		upvote_ob = datastore.upvotes[topic_id]
		upvote_ob.upvotes += 1
		datastore.top_topics.add_upvote(topic_id, upvote_ob.upvotes)
		return success_response(upvote_ob)

	except Exception as e:
		app.logger.error("Some unexpected error has occured.")
		return internal_error("Some unexpected error has occured.")
