# -*- coding: utf-8 -*-

from reddit.app import app, datastore

def set_current_user(user):
	datastore.current_user = user

def unset_current_user():
	datastore.current_user = None

def is_authenticated():
	if datastore.current_user:
		return True

	return False
