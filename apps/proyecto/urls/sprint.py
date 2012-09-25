from django.conf.urls.defaults import patterns, url
from apps.proyecto.views import sprint as s

urlpatterns = patterns('',
                       url(r'^sprint/list/(?P<pk>\d+)$',s.sprintlist.as_view(),name='Lista_sprint_view'),
                       url(r'^sprint/(?P<pk>\d+)/new/$',s.newSprint.as_view(),name='new_sprint_view'),
                       url(r'^sprint/edit/(?P<pk>\d+)$',s.editSprint.as_view(),name='edit_sprint_view'),
                       url(r'^sprint/del/(?P<pk>\d+)$',s.delSprint.as_view(),name='del_sprint_view'),
                       )