# -*- coding: utf-8 -*-

from reddit.app import app
from flask import request
from reddit.controller.upvote import create_upvote
import json

@app.route('/upvote', methods = ['POST'])
def upvote():
	if request.method == 'POST':
		response = create_upvote(request.json)

		return response
