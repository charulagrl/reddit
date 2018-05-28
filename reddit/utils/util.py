from reddit.store import datastore
from reddit.models.topic import Topic
from reddit.app import datastore
import uuid

def create_topic(content):
	new_id = str(uuid.uuid4())
	while (datastore.topics.get(new_id, None)):
		new_id = str(uuid.uuid4())
	
	topic = Topic(topic_id=new_id, content=content)

	datastore.topics[new_id] = topic
	datastore.upvotes[new_id] = 0
	datastore.downvotes[new_id] = 0

	return topic

def create_upvote(topic_id):
	topic = datastore.topics.get(topic_id, None)

	if topic:
		datastore.upvotes[topic_id] += 1

	return datastore.upvotes[topic_id]

def create_downvote(topic_id):
	topic = datastore.topics.get(topic_id, None)

	if topic:
		datastore.downvotes[topic_id] += 1

	return datastore.downvotes[topic_id]
