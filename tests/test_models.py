# -*- coding: utf-8 -*-

import pytest
from reddit.models.user import User
from reddit.models.topic import Topic
from reddit.models.upvote import Upvote
from reddit.models.downvote import Downvote


def test_new_user(new_user):
	assert new_user.user_id == "abc"

def test_new_topic(new_user, new_topic):
	assert new_topic.id == 1
	assert new_topic.user_id == "abc"
	assert new_topic.content == "test"

def test_new_upvote(new_topic):
	upvote = Upvote()
	upvote.add_upvote(new_topic.id)
	assert upvote.get_upvotes(new_topic.id) == 1
	upvote.add_upvote(new_topic.id)
	assert upvote.get_upvotes(new_topic.id) == 2

def test_new_downvote(new_topic):
	downvote = Downvote()
	downvote.add_downvote(new_topic.id)
	assert downvote.get_downvotes(new_topic.id) == 1
	downvote.add_downvote(new_topic.id)
	assert downvote.get_downvotes(new_topic.id) == 2
