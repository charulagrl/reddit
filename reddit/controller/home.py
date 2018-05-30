# -*- coding: utf-8 -*-

from flask import request
from reddit.app import app, datastore
from reddit.utils.errors import internal_error
from reddit.utils.errors import not_found
from reddit.utils.errors import bad_request
from reddit.utils.success import success_response, success_list_response

import uuid
import json

def get_top_topics():
	topics_counter = datastore.upvotes.get_top_topics()
	topics = [datastore.topics[topic_id].__dict__ for (topic_id, counter) in topics_counter]

	for topic in topics:
		topic["upvotes"] = datastore.upvotes.counter[topic['id']]
		topic["downvotes"] = datastore.downvotes.counter[topic['id']]

	return success_list_response(topics)
