from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]


handler400 = 'src.utils.error400View'
handler403 = 'src.utils.error403View'
handler404 = 'src.utils.error404View'
handler405 = 'src.utils.error405View'
handler500 = 'src.utils.error500View'