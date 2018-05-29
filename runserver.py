# -*- coding: utf-8 -*-

from logging.handlers import RotatingFileHandler
import logging
import os

if not os.environ.get("REDDIT_CONFIG"):
    os.environ["REDDIT_CONFIG"] = '../../development.cfg'

from reddit.app import app

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = RotatingFileHandler('service.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.ERROR)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

app.run()