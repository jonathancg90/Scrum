from django.conf.urls.defaults import patterns, url
from apps.proyecto.views import proyecto as p


urlpatterns = patterns('',
                       url(r'^proy/list/$',p.proylist.as_view(),name='Lista_view'),
                       url(r'^proy/new/$',p.newProject.as_view(),name='new_project_view'),
                       url(r'^proy/edit/(?P<pk>\d+)$',p.editProject.as_view(),name='edit_project_view'),
                       url(r'^proy/del/(?P<pk>\d+)$',p.delProject.as_view(),name='del_project_view'),
                       #url(r'^sprint/list/(?P<pk>\d+)$',s.sprintlist.as_view(),name='Lista_sprint_view'),
                       )