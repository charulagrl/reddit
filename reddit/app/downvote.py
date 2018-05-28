# -*- coding: utf-8 -*-

from reddit.app import app
from flask import url_for, request, redirect
from reddit.utils.util import create_downvote
from reddit.app import datastore

@app.route('/downvote', methods = ['POST'])
def downvote():
	if request.method == 'POST':
		topic_id = request.json['topic_id']
		print topic_id
		count = create_downvote(topic_id)

		return str(count)