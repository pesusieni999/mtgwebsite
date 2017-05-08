#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to populate database for testing purposes.
"""

import os
import django
import pytz
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.contrib.auth.models import User
from mtgapp.models import Game, SignUp

__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


def populate():
    """
    Populate the database with information defined in this function.
    :return: Nothing.
    """

    # Times
    d = datetime(2017, 12, 1, 10, 0, tzinfo=pytz.utc)

    # Create superusers.
    super_users_created = 0
    super_users_updated = 0
    s_user, created = add_super_user('nimda', '1234')
    if created:
        super_users_created += 1
    else:
        super_users_updated += 1

    # Create games.
    games_created = 0
    games_updated = 0
    g, created = add_game(s_user, "Commander (budget)", "Metropolis", d)
    if created:
        games_created += 1
    else:
        games_updated += 1

    # Sign-ups
    sign_ups_created = 0
    s, created = add_sign_ups(s_user, g)
    if created:
        sign_ups_created += 1

    # Print populate results.
    print('Super users created: ', super_users_created)
    print('Super users updated: ', super_users_updated)
    print('Games created: ', games_created)
    print('Games updated: ', games_updated)
    print('Sign-ups created: ', games_created)


def add_super_user(name, password):
    """
    Add or get super user. Matching name is considered same.
    :param name: Name of the user.
    :param password: New password.
    :return: Created/Updated user object, Boolean (true if user created).
    """
    created = False
    try:
        u = User.objects.get(username=name)
    except User.DoesNotExist:
        created = True
        u = User(username=name)
    u.set_password(password)
    u.save()
    return u, created


def add_game(owner, game_format, location, time):
    """
    Add or get game object. Matching owner+time is considered same.
    :param owner: User object (game creator)
    :param game_format: String telling format of the game.
    :param location: String telling location of the game.
    :param time: DateTime object telling game start time.
    :return: Created/Updated game object, Boolean (true if game created).
    """
    created = False
    try:
        g = Game.objects.get(owner=owner, time=time)
        g.format = game_format
        g.location = location
    except Game.DoesNotExist:
        created = True
        g = Game(owner=owner, format=game_format, location=location, time=time)
    g.save()
    return g, created


def add_sign_ups(user, game):
    """
    Add sign-up object. Matching user+game is considered same.
    :param user: User object.
    :param game: Game object.
    :return: Sign-up object, Boolean (true if created).
    """
    created = False
    try:
        s = SignUp.objects.get(user=user, game=game)
    except SignUp.DoesNotExist:
        created = True
        s = SignUp(user=user, game=game)
        s.save()
    return s, created


if __name__ == '__main__':
    print('Starting database test data population.')
    populate()
    print('Test data population completed.')
