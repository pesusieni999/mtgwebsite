"""
Define URLs routing for MtG application.
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
    url(r'^games/$', views.Games.as_view(), name='games'),
    url(r'^games/(?P<game_id>\d+)/$', views.GameView.as_view(), name='game'),
    url(r'^games/(?P<game_id>\d+)/delete/$', views.DeleteGameView.as_view(), name='delete_game'),
    url(r'^games/(?P<game_id>\d+)/signup/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^games/(?P<game_id>\d+)/signup/delete$', views.DeleteSignUpView.as_view(), name='delete_sign_up'),
]
