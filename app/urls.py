from django.urls import path
from .views import *

urlpatterns = [
	path('', indexView, name='home'),
	path('git/pull', gitPull),
	path('user', indexView, name='user'),
	path('test2', testView, name='test'),
]

