# -*- coding: utf-8 -*-

from reddit.utils.request_type import request_wants_html
from reddit.utils.success import success_list_response
from reddit.controller.home import get_top_topics
from flask import request, render_template
from reddit.app import app
import json

@app.route('/home', methods = ['GET'])
def home():
	topics = get_top_topics()

	if request_wants_html():
		return render_template('home.html', topics=topics)
	else:
		return success_list_response(topics)
