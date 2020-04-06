from django.shortcuts import render

def error400View(request, *args, **argv):
	content = {}
	content['error'] = '400'
	content['desc'] = 'Bad Request'
	return render(request, 'error.html', content)

def error403View(request, *args, **argv):
	content = {}
	content['error'] = '403'
	content['desc'] = 'Invalid Permissions'
	return render(request, 'error.html', content)

def error404View(request, *args, **argv):
	content = {}
	content['error'] = '404'
	content['desc'] = 'Page Not Found'
	return render(request, 'error.html', content)

def error405View(request, *args, **argv):
	content = {}
	content['error'] = '405'
	content['desc'] = 'Unknown'
	return render(request, 'error.html', content)

def error500View(request, *args, **argv):
	content = {}
	content['error'] = '500'
	content['desc'] = 'Internal Server Problem'
	return render(request, 'error.html', content)
