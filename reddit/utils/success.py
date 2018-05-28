# -*- coding: utf-8 -*-

from flask import Response
import traceback
import json

def success_response(ob):
	return Response(
		response=json.dumps(ob.__dict__),
		status=200,
		mimetype='application/json'
	)
