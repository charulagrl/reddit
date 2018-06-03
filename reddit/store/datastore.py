# -*- coding: utf-8 -*-

from reddit.models.upvote import Upvote
from reddit.models.downvote import Downvote


class DataStore(object):
	def __init__(self):
		self.topics = {}
		self.upvotes = Upvote()
		self.downvotes = Downvote()
		self.users = {}
		self.current_user = None

	def get_topic(self, topic_id):
		topic = self.topics.get(topic_id, None)
		if topic:
			topic = topic.__dict__
			topic["upvotes"] = self.upvotes.get_upvotes(topic['id'])
			topic["downvotes"] = self.downvotes.get_downvotes(topic['id'])

		return topic

	def get_upvotes(self, topic_id):
		upvotes = self.upvotes.get(topic_id, None)

		return upvotes

	def get_downvotes(self, topic_id):
		downvotes = self.downvotes.get(topic_id, None)

		return downvotes

	def get_user(self, user_id):
		users = self.users.get(user_id, None)

		return users

	def get_all_topics(self):
		topics = [self.topics[topic].__dict__ for topic in self.topics.keys()]

		for topic in topics:
			topic["upvotes"] = self.upvotes.get_upvotes(topic['id'])
			topic["downvotes"] = self.downvotes.get_downvotes(topic['id'])

		return topics
