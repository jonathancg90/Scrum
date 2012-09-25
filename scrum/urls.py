from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^scrum/',include('apps.proyecto.urls.session')),
                       url(r'^scrum/',include('apps.proyecto.urls.proyecto')),
                       url(r'^scrum/',include('apps.proyecto.urls.sprint')),
                       url(r'^scrum/',include('apps.proyecto.urls.story')),      
                       )