"""
Database models related to MtG application.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class Game(models.Model):
    """
    Model for MtG games.
    """
    owner = models.ForeignKey(User, related_name='games', on_delete=models.CASCADE)
    format = models.CharField(max_length=64)
    time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=128)
    max_sign_ups = models.IntegerField(default=10)
    participants = models.ManyToManyField(
        User,
        through="SignUp",
        related_name="game_sign_ups"
    )

    class Meta:
        ordering = ['-time']


class SignUp(models.Model):
    """
    Model for Sign-ups.
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    commander = models.CharField(max_length=64, blank=True)
    deck = models.URLField(max_length=128, blank=True)

    class Meta:
        ordering = ['-time']


class MtgCard(models.Model):
    """
    Model for MtG card that is used.
    """
    name = models.CharField(max_length=128)
    # Used for fetching image and other information from MtG API.
    url = models.CharField(max_length=512)
