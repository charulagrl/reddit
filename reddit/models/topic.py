# -*- coding: utf-8 -*-

class Topic(object):
	def __init__(self, topic_id, content):
		self.id = topic_id
		self.content = content

	def get_topic_id(self):
		return self.id

	def get_content(self):
		return self.content

	def __str__(self):
		return "topic_id " + self.id + " content " + self.content

