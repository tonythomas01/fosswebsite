from django.conf.urls import *
from achievement import views

urlpatterns = patterns('',
    url(r'^/viewall/$',views.achieve_viewall),
    url(r'^/contribution/$', views.contrib_viewall),
    url(r'^/articles/$', views.article_viewall),
    url(r'^/gsoc/$', views.gsoc_viewall),
    url(r'^/speakers/$', views.speaker_viewall),
    url(r'^/interns/$', views.intern_viewall),
    url(r'^/contests/$', views.contest_won_viewall),
    url(r'^/icpc/$', views.icpc_viewall),
) 
