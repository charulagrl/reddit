# -*- coding: utf-8 -*-

from flask import request
from reddit.controller import topic
from reddit.app import app
import json

@app.route('/topic', methods = ['POST'])
def create_topic():
	if request.method == 'POST':
		response = topic.create_topic(request.json)

		return response

@app.route('/topic/<topic_id>')
def get_topic(topic_id):
	response = topic.get_topic(topic_id)

	return response

@app.route('/list/topics')
def all_topics():
	response = topic.get_all_topics()
	
	return response
