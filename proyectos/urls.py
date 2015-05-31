from django.conf.urls import patterns, url
from proyectos import views

urlpatterns = patterns('',
    # /proyectos/
    url(r'^$', views.index, name='index'),
    # /proyectos/5/
    url(r'^(?P<id_proyecto>\d+)/$', views.proyecto, name='proyecto'),
    # /proyectos/nuevo_proyecto
    url(r'^nuevo_proyecto/$', views.nuevo_proyecto, name='nuevo_proyecto'),
    # /proyectos/terminados
    url(r'^terminados/$', views.terminados, name='terminados'),
    # /proyectos/5/2/
    url(r'^(?P<id_proyecto>\d+)/(?P<id_tarea>\d+)/$', views.tarea, name='tarea'),
    # /proyectos/tareas_terminadas
    url(r'^tareas_terminadas/$', views.tareas_terminadas, name='tareas_terminadas'),
    # /proyectos/login/
    url(r'^login/$', views.web_login, name='login'),
    # /proyectos/logout/
    url(r'^logout/$', views.web_logout, name='logout'),
    # /proyectos/usuarios/
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    # /proyectos/usuarios/20
    url(r'^usuarios/(?P<id_usuario>\d+)/$', views.usuario, name='usuario'),
    # /proyectos/usuarios/20/baja
    url(r'^usuarios/(?P<id_usuario>\d+)/baja/$', views.baja, name='baja'),
)

urlpatterns += patterns('',
 (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )
