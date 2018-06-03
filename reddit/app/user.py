# -*- coding: utf-8 -*-

from reddit.utils.request_type import request_wants_html
from reddit.utils.success import success_response
from flask import request, render_template, flash, redirect, url_for
from reddit.controller import user
from reddit.models.user import User
from reddit.app import app, datastore
from reddit.utils.form import UserForm, LoginForm
from reddit.utils.current_user import is_authenticated
import json

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
	if request_wants_html():
		form = UserForm(request.form)
		if request.method == 'POST' and form.validate():
			new_user = user.create_user_html(form)
			return render_template("user_created.html", user=new_user)

		return render_template('signup.html', form=form)
	else:
		return user.create_user(request)

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if is_authenticated():
		return redirect(url_for("home"))

	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user.user_login(form)
		return render_template("home.html")
	return render_template('login.html', form=form)