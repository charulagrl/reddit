# -*- coding: utf-8 -*-
from reddit.app import app

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    return "Welcome to reddit clone app!"
