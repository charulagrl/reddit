# -*- coding: utf-8 -*-

from reddit.models.upvote import Upvote

class DataStore(object):
	def __init__(self):
		self.topics = {}
		self.upvotes = Upvote()
		self.downvotes = {}
		self.users = {}
		# self.top_topics = TopTopics()

	def get_topic(self, topic_id):
		topic = self.topics.get(topic_id, None)

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
