# -*- coding: utf-8 -*-

from reddit.app import app
from flask import url_for, request, redirect
from reddit.utils.util import create_topic
from reddit.app import datastore


@app.route('/topic', methods = ['POST'])
def topic():
	if request.method == 'POST':
		content = request.json['content']

		topic = create_topic(content)

		return str(topic)

@app.route('/list/topics')
def all_topics():
	return str(datastore.topics)
