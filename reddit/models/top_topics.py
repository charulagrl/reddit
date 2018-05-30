# -*- coding: utf-8 -*-

from collections import Counter

class TopTopics(object):

	def __init__(self):
		self.counter = Counter()

	def add_upvote(self, topic_id, upvotes):
		self.counter[topic_id] = upvotes

	def get_top_topics(self, n=20):
		return self.counter.most_common(n)