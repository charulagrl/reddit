# -*- coding: utf-8 -*-

from logging.handlers import RotatingFileHandler
from flask import request
import logging
import os

if not os.environ.get("REDDIT_CONFIG"):
    os.environ["REDDIT_CONFIG"] = '../../development.cfg'

from reddit.app import app

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s")
handler = RotatingFileHandler('service.log', maxBytes=10000, backupCount=1)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

app.run()