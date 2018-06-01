# -*- coding: utf-8 -*-

from reddit.utils.request_type import request_wants_html
from flask import request, render_template
from reddit.controller import user
from reddit.models.user import User
from reddit.utils.success import success_response
from reddit.app import app
from reddit.utils.form import UserForm
import json

@app.route('/user', methods = ['POST', 'GET'])
def create_user():
	if request_wants_html():
		form = UserForm(request.form)
		if request.method == 'POST' and form.validate():
			new_user = user.create_user_html(form)
			return render_template("user_created.html", user=new_user)

		return render_template('user.html', form=form)
	else:
		return user.create_user(request)
