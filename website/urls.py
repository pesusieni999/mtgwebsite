"""
URL routing for main application.

This will reroute requests to sub applications when needed.
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from . import views


__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', views.Register.as_view(), name='register'),
]
