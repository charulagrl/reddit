# -*- coding: utf-8 -*-

from flask import Flask
from reddit.store.datastore import DataStore

app = Flask(__name__)
app.config.from_envvar('REDDIT_CONFIG')
datastore = DataStore()

from reddit.app import index
from reddit.app import topic
from reddit.app import upvote
from reddit.app import downvote
