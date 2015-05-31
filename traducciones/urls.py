from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from proyectos import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^proyectos/', include('proyectos.urls', namespace="proyectos"))
)# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Donde se guardan archivos

