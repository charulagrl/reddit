# -*- coding: utf-8 -*-

from flask import url_for, request, redirect, Response
from reddit.store import datastore
from reddit.models.topic import Topic
from reddit.models.upvote import Upvote
from reddit.models.downvote import Downvote
from reddit.app import datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request

import uuid
import json

def create_topic(request_data):
	if not request_data.get('content', None):
		return bad_request("Content is missing")

	content = request_data['content']
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

def create_upvote(request_data):
	if not request_data.get('topic_id', None):
		return bad_request("Topic id is missing")

	topic_id = request_data['topic_id']
	topic = datastore.topics.get(topic_id, None)

	if not topic:
		return not_found("Topic with id %s does not exist"%topic_id)

	upvote_ob = datastore.upvotes[topic_id]
	upvote_ob.upvotes += 1

	return success_response(upvote_ob)

def create_downvote(topic_id):
	if not request_data.get('topic_id', None):
		return bad_request("Topic id is missing")

	topic_id = request_data['topic_id']
	topic = datastore.topics.get(topic_id, None)

	if not topic:
		return not_found("Topic with id %s does not exist"%topic_id)

	downvote_ob = datastore.downvotes[topic_id]
	downvote_ob.downvotes += 1

	return success_response(downvote_ob)

def success_response(ob):
	return Response(
			response=json.dumps(ob.__dict__),
			status=200,
			mimetype='application/json'
		)
