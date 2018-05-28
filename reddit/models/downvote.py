# -*- coding: utf-8 -*-

class Downvote(object):
	def __init__(self, topic_id):
		self.id = topic_id
		self.downvotes = 0

	def get_topic_id(self):
		return self.id

	def get_downvotes(self):
		return self.downvotes
