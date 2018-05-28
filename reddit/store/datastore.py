class DataStore(object):
	def __init__(self):
		self.topics = {}
		self.upvotes = {}
		self.downvotes = {}

	def get_topic(self, topic_id):
		topic = self.topics.get(topic_id, None)

		return topic

	def get_upvotes(self, topic_id):
		upvotes = self.upvotes.get(topic_id, None)

		return upvotes

	def get_downvotes(self, topic_id):
		downvotes = self.downvotes.get(topic_id, None)

		return downvotes
