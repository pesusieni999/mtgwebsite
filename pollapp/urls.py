"""
Define URLs routing for Polls application.
"""

from django.conf.urls import url
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
    url(r'^$', views.Polls.as_view(), name='polls'),
    url(r'^(?P<poll_id>\d+)/$', views.PollView.as_view(), name='poll'),
    url(
        r'^(?P<poll_id>\d+)/delete/$',
        views.DeletePoll.as_view(),
        name='delete_poll'
    ),
    url(
        r'^(?P<poll_id>\d+)/options/$',
        views.PollOptionsView.as_view(),
        name='poll_options'
    ),
    url(r'^(?P<poll_id>\d+)/vote/$', views.VoteView.as_view(), name='vote'),
    url(
        r'^(?P<poll_id>\d+)/vote/delete/$',
        views.DeleteVote.as_view(),
        name='delete_vote'
    ),
]
