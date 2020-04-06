from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import Http404
from django.conf import settings
import git
import json
import os
# Create your views here.

def indexView(request):
	return HttpResponse('Home Page')

def userView(request):
	return HttpResponse('User Page')

@csrf_exempt
def gitPull(request):
	if request.method == 'POST':
		if settings.DEBUG:
			repo = git.Repo(settings.BASE_DIR)
			origin = repo.remotes.origin
			origin.pull()

			os.system('touch /var/www/ctavares94_pythonanywhere_com_wsgi.py')
			return HttpResponse('Updated successfully')
		else:
			return HttpResponse('Error')
	raise Http404()
	return HttpResponseRedirect(reverse_lazy('404'))