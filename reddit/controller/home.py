# -*- coding: utf-8 -*-

from reddit.utils.errors import internal_error, not_found, bad_request
from reddit.utils.success import success_response, success_list_response
from reddit.app import datastore

def get_top_topics():
	topics_counter = datastore.upvotes.get_top_topics()
	topics = [datastore.topics[topic_id].__dict__ for (topic_id, counter) in topics_counter]

	for topic in topics:
		topic["upvotes"] = datastore.upvotes.get_upvotes(topic['id'])
		topic["downvotes"] = datastore.downvotes.get_downvotes(topic['id'])

	return topics
