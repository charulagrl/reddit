# -*- coding: utf-8 -*-

from flask import url_for, request, redirect, Response
from reddit.utils.util import create_topic
from reddit.app import app, datastore
import json

@app.route('/topic', methods = ['POST'])
def topic():
	if request.method == 'POST':
		response = create_topic(request.json)

		return response

@app.route('/list/topics')
def all_topics():
	return str(datastore.topics)
