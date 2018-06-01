# -*- coding: utf-8 -*-

from reddit.app import app
from flask import Response, render_template
from reddit.utils.request_type import request_wants_html
import json

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
	if request_wants_html():
		return render_template('index.html')
	else:
		return Response(
			response=json.dumps("Welcome to reddit clone app!"),
			status=200,
			mimetype='application/json'
		)
