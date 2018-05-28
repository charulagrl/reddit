# -*- coding: utf-8 -*-

from flask import request, Response
from reddit.controller.downvote import create_downvote
from reddit.app import app
import json

@app.route('/downvote', methods = ['POST'])
def downvote():
	if request.method == 'POST':
		response = create_downvote(request.json)

		return response