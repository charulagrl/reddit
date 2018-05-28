# -*- coding: utf-8 -*-

from reddit.app import app
from flask import url_for, request, redirect, Response
from reddit.utils.util import create_upvote
from reddit.app.errors import bad_request
import json

@app.route('/upvote', methods = ['POST'])
def upvote():
	if request.method == 'POST':
		response = create_upvote(request.json)

		return response
