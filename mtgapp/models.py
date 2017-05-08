from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Game(models.Model):
    owner = models.ForeignKey(User, related_name='games', on_delete=models.CASCADE)
    format = models.CharField(max_length=64)
    time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=128)
    participants = models.ManyToManyField(
        User,
        through="SignUp",
        related_name="game_sign_ups"
    )


class SignUp(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MtgCard(models.Model):
    """
    Model for MtG card that is used.
    """
    name = models.CharField(max_length=128)
    # Used for fetching image and other information from MtG API.
    url = models.CharField(max_length=512)
