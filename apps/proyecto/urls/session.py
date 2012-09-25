from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.proyecto.views.session',
                       url(r'^login/$','loginUser',name='login_view'),
                       url(r'^logout/$','logout',name='logout_view'),

)