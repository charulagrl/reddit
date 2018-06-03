# -*- coding: utf-8 -*-

import pytest
import json

def test_home_page(test_client):
	response = test_client.get('/index/')
	assert response.status_code == 200


def test_user_page(test_client):
	mimetype = 'application/json'
	headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
	response = test_client.post('/signup', data=json.dumps({"user_id": "abc"}), headers=headers,
		follow_redirects=True)
	assert response.status_code == 200
	assert response.json['user_id'] == "abc"


def test_topic_page(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

	response = test_client.post('/topic', data=json.dumps({"user_id": new_user.user_id, "content": "test"}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 200
	assert response.json['content'] == "test"
	assert response.json["user_id"] == new_user.user_id

def test_topic_page_with_400_error(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

	response = test_client.post('/topic', data=json.dumps({"user_id": new_user.user_id}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 400

def test_topic_page_with_404_error(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

	response = test_client.post('/topic', data=json.dumps({"user_id": 123, "content": "aa"}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 404

def test_upvote_page(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}
	topic_response = test_client.post('/topic', data=json.dumps({"user_id": new_user.user_id, "content": "test"}),
		headers=headers, follow_redirects=True)
	topic_id = topic_response.json["id"]

	response = test_client.post('/upvote/'+topic_id, data=json.dumps({"user_id": new_user.user_id}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 200
	assert response.json['upvotes'] == 1

def test_upvote_page_with_404_error(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

	response = test_client.post('/upvote/123', data=json.dumps({"user_id": new_user.user_id}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 404

def test_upvote_page_with_400_error(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}
	topic_response = test_client.post('/topic', data=json.dumps({"user_id": new_user.user_id, "content": "test"}), 
		headers=headers, follow_redirects=True)
	topic_id = topic_response.json["id"]

	response = test_client.post('/upvote/'+topic_id, data=json.dumps({"user": new_user.user_id}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 400

def test_downvote_page(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

	topic_response = test_client.post('/topic', data=json.dumps({"user_id": new_user.user_id, "content": "test"}), 
		headers=headers, follow_redirects=True)
	topic_id = topic_response.json["id"]

	response = test_client.post('/downvote/'+topic_id, data=json.dumps({"user_id": new_user.user_id}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 200
	assert response.json['downvotes'] == 1

def test_downvote_page_with_404_error(test_client, new_user):
	mimetype = 'application/json'
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

	topic_response = test_client.post('/topic', data=json.dumps({"user_id": new_user.user_id, "content": "test"}), 
		headers=headers, follow_redirects=True)
	topic_id = topic_response.json["id"]

	response = test_client.post('/downvote/'+topic_id, data=json.dumps({"user_id": 123}),
		headers=headers, follow_redirects=True)
	assert response.status_code == 404
