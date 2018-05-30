# -*- coding: utf-8 -*-

from reddit.app import app
from flask import request
from reddit.controller.home import get_top_topics
import json

@app.route('/home', methods = ['GET'])
def top_topics():
	response = get_top_topics()

	return response
