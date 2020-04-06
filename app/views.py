from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
import git
import json
# Create your views here.

def indexView(request):
	return HttpResponse('Home Page')

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