import os

if not os.environ.get("REDDIT_CONFIG"):
	os.environ["REDDIT_CONFIG"] = '../../development.cfg'