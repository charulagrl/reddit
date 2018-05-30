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

port = int(os.environ.get("PORT", 33507))
app.run(host="0.0.0.0", port=port)