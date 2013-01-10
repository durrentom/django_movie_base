from django.conf.urls import patterns, include, url
from movies.views import *

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^now/$', now),
	url(r'^movies/$', movies),
	url(r'^movie/(?P<slug>[\w-]+)/$', movie_details),
	url(r'^director/(?P<slug>[\w-]+)/$', director_details),
)
