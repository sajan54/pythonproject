def application(environ, start_response):
	status = '200OK'
	output = b'Hello World! CI/CD pipeline testing for python'
	response_headers = [('Content-type', 'text/plain'),
				('Content-Length', str(len(output)))]
	start_response(status, response_headers)
	return [output]
