# -*- coding: utf-8 -*-

from reddit.controller.upvote import create_upvote_json, create_upvote_html
from reddit.utils.request_type import request_wants_html
from reddit.utils.current_user import is_authenticated
from reddit.app import app
from flask import request, redirect, url_for
import json

@app.route('/upvote/<topic_id>', methods = ['POST', 'GET'])
def upvote(topic_id):
	if request_wants_html():
		if not is_authenticated():
			return redirect(url_for('login'))

		if request.method == 'GET':
			response = create_upvote_html(topic_id)

			return redirect(url_for('get_topic', topic_id=topic_id))
	else:
		if request.method == 'POST':
			response = create_upvote_json(request.json, topic_id)
			return response
