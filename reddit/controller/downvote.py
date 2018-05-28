# -*- coding: utf-8 -*-

from flask import request, Response
from reddit.store import datastore
from reddit.models.topic import Topic
from reddit.models.upvote import Upvote
from reddit.models.downvote import Downvote
from reddit.app import datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response

import uuid
import json

def create_downvote(request_data):
	if not request_data.get('topic_id', None):
		return bad_request("Topic id is missing")

	topic_id = request_data['topic_id']
	topic = datastore.topics.get(topic_id, None)

	if not topic:
		return not_found("Topic with id %s does not exist"%topic_id)

	downvote_ob = datastore.downvotes[topic_id]
	downvote_ob.downvotes += 1

	return success_response(downvote_ob)
