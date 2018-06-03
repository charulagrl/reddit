# -*- coding: utf-8 -*-

from reddit.utils.success import success_dict_response, success_list_response
from reddit.utils.request_type import request_wants_html
from reddit.utils.form import TopicForm, UpvoteForm
from reddit.utils.current_user import is_authenticated
from flask import request, render_template, flash, redirect, url_for
from reddit.controller import topic
from reddit.app import app
import json

@app.route('/topic', methods = ['POST', 'GET'])
def create_topic():
	if request_wants_html():
		if not is_authenticated():
			return redirect(url_for('login'))

		form = TopicForm(request.form)
		if request.method == 'POST' and form.validate():
			new_topic = topic.create_topic_html(form)
			return render_template("topic_created.html", topic=new_topic)

		return render_template('topic.html', form=form)
	else:
		if request.method == 'POST':
			return topic.create_topic_json(request.json)

@app.route('/topic/<topic_id>')
def get_topic(topic_id):
	topic_ob = topic.get_topic(topic_id)
	form = UpvoteForm(request.form)
	if request_wants_html():
		return render_template('single_topic.html', topic=topic_ob, form=form)
	else:
		return success_dict_response(topic_ob)

@app.route('/list/topics')
def all_topics():
	response = topic.get_all_topics()
	if request_wants_html():
		return render_template('all_topics.html', topics=response)
	else:
		return response
