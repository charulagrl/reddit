# -*- coding: utf-8 -*-

class User(object):
	def __init__(self, user_id):
		self.user_id = user_id

	def get_user_id(self):
		return self.user_id

	def __str__(self):
		return "user id is " + self.user_id