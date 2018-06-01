# -*- coding: utf-8 -*-

from reddit.utils.request_type import request_wants_html
from reddit.utils.form import TopicForm
from flask import request, render_template
from reddit.controller import topic
from reddit.app import app
import json

@app.route('/topic', methods = ['POST', 'GET'])
def create_topic():
	if request_wants_html():
		form = TopicForm(request.form)
		if request.method == 'POST' and form.validate():
			new_topic = topic.create_topic_html(form)
			return render_template("topic_created.html", topic=new_topic)

		return render_template('topic.html', form=form)
	else:
		if request.method == 'POST':
			response = topic.create_topic(request.json)

			return response

@app.route('/topic/<topic_id>')
def get_topic(topic_id):
	response = topic.get_topic(topic_id)

	return response

@app.route('/list/topics')
def all_topics():
	response = topic.get_all_topics()
	
	return response
