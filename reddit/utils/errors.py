# -*- coding: utf-8 -*-

from flask import Response
import traceback
import json

def internal_error(error):
    return Response(
        response=json.dumps({
            'error': 'internal_error',
            'detail': str(error),
            'traceback': traceback.format_exc(),
        }),
        status=500,
        mimetype='application/json',
    )

def not_found(error):
    return Response(
        response=json.dumps({'error': error}),
        status=404,
        mimetype='application/json',
    )

def bad_request(error):
    return Response(
        response=json.dumps({
            'error': 'bad request',
            'detail': str(error),
        }),
        status=400,
        mimetype='application/json',
    )
