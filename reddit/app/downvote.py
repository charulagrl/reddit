# -*- coding: utf-8 -*-

from reddit.controller.downvote import create_downvote_json, create_downvote_html
from reddit.utils.request_type import request_wants_html
from reddit.utils.current_user import is_authenticated
from flask import request, redirect, url_for
from reddit.app import app
import json

@app.route('/downvote/<topic_id>', methods = ['POST', 'GET'])
def downvote(topic_id):
	if request_wants_html():
		if not is_authenticated():
			return redirect(url_for('login'))

		if request.method == 'GET':
			response = create_downvote_html(topic_id)

			return redirect(url_for('get_topic', topic_id=topic_id))
	else:
		if request.method == 'POST':
			response = create_downvote_json(request.json, topic_id)
			return response