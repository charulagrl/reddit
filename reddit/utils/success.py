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

def success_dict_response(ob):
	return Response(
		response=json.dumps(ob),
		status=200,
		mimetype='application/json'
	)

def success_list_response(response_list):
	return Response(
		response=json.dumps(response_list),
		status=200,
		mimetype='application/json'
	)
