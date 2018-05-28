# -*- coding: utf-8 -*-

from reddit.app import app
from flask import url_for, request, redirect
from reddit.utils.util import create_upvote

@app.route('/upvote', methods = ['POST'])
def upvote():
	if request.method == 'POST':
		topic_id = request.json['topic_id']
		count = create_upvote(topic_id)

		return str(count)
