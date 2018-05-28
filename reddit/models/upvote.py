# -*- coding: utf-8 -*-

class Upvote(object):
	def __init__(self, topic_id):
		self.id = topic_id
		self.upvotes = 0

	def get_topic_id(self):
		return self.id

	def get_upvotes(self):
		return self.upvotes
