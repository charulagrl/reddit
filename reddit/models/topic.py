# -*- coding: utf-8 -*-

class Topic(object):
	def __init__(self, topic_id, content, user_id):
		self.id = topic_id
		self.content = content
		self.user_id = user_id
		print "dacscsd"

	def get_topic_id(self):
		return self.id

	def get_content(self):
		return self.content

	def __str__(self):
		return "topic_id is " + self.id + " and content is " + self.content

