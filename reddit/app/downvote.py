# -*- coding: utf-8 -*-

from flask import url_for, request, redirect, Response
from reddit.utils.util import create_downvote
from reddit.app.errors import bad_request
from reddit.app import app, datastore
import json

@app.route('/downvote', methods = ['POST'])
def downvote():
	if request.method == 'POST':
		response = create_downvote(request.json)

		return response