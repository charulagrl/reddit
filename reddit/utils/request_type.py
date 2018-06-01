from flask import Flask, request

def request_wants_html():
	best = request.accept_mimetypes \
		.best_match(['application/json', 'text/html', 'text/plain'])
	return best == 'text/html'
