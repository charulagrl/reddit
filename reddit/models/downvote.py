# -*- coding: utf-8 -*-

from collections import Counter

class Downvote(object):
	def __init__(self):
		self.counter = Counter()

	def add_downvote(self, topic_id):
		count = self.counter.get(topic_id, None)
		if count:
			self.counter[topic_id] += 1
		else:
			self.counter[topic_id] = 1

		return self.counter[topic_id]

	def create_downvote(self, topic_id):
		self.counter[topic_id] = 0

	def get_downvotes(self, topic_id):
		return self.counter.get(topic_id, None)
