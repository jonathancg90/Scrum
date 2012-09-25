from django.conf.urls.defaults import patterns, url
from apps.proyecto.views import story as s

urlpatterns = patterns('',
                       url(r'^story/list/(?P<pk>\d+)$',s.storylist.as_view(),name='Lista_story_view'),
                       url(r'^story/(?P<pk>\d+)/new/$',s.newStory.as_view(),name='new_story_view'),
                       url(r'^story/edit/(?P<pk>\d+)$',s.editStory.as_view(),name='edit_story_view'),
                       url(r'^story/del/(?P<pk>\d+)$',s.delStory.as_view(),name='del_story_view'),
                       )