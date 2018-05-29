# -*- coding: utf-8 -*-

from flask import request
from reddit.controller import user
from reddit.app import app
import json

@app.route('/user', methods = ['POST'])
def create_user():
	if request.method == 'POST':
		response = user.create_user(request.json)

		return response