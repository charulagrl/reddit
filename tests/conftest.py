# -*- coding: utf-8 -*-

import pytest
from reddit.models.user import User
from reddit.models.topic import Topic
from flask import Flask
from reddit import app

@pytest.fixture(scope='module')
def new_user():
	user = User(user_id="abc")
	return user

@pytest.fixture(scope='module')
def new_topic(new_user):
	topic = Topic(user_id=new_user.user_id, content="test", topic_id=1)
	return topic

@pytest.fixture(scope='module')
def test_client():
    testing_client = app.app.test_client()
    return testing_client 
