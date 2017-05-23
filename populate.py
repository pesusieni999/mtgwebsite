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
from pollapp.models import Poll, PollAnswer, PollOption


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
    # No need to update, since nothing to update.

    # Polls
    polls_created = 0
    polls_updated = 0
    p, created = add_poll(
        s_user,
        "Increase infect limit",
        "Should we increase lethal infect damage limit in commander?",
        True,
        d
    )
    if created:
        polls_created += 1
    else:
        polls_updated += 1

    # Poll options.
    poll_options_created = 0
    o_one, created = add_poll_option("Yes, to 20", p)
    if created:
        poll_options_created += 1
    o_two, created = add_poll_option("Yes, to 30", p)
    if created:
        poll_options_created += 1
    o_three, created = add_poll_option("No, keep at 10", p)
    if created:
        poll_options_created += 1
    # No need to update, since nothing to update.

    # Poll answers
    poll_answers_created = 0
    a, created = add_poll_answers(s_user, o_one)
    if created:
        poll_answers_created += 1
    # No need to update, since nothing to update.

    # Print populate results.
    print('Super users created:\t', super_users_created)
    print('Super users updated:\t', super_users_updated)
    print('Games created:\t\t', games_created)
    print('Games updated:\t\t', games_updated)
    print('Sign-ups created:\t', sign_ups_created)
    print('Polls created:\t\t', polls_created)
    print('Polls updated:\t\t', polls_updated)
    print('Poll options created:\t', poll_options_created)
    print('Poll answers created:\t', poll_answers_created)


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


def add_poll(owner, name, question, single_selection, end_time):
    """
    Add poll object. Matching owner+name is considered same.
    :param owner: User object.
    :param name: Name for poll.
    :param question: Poll question.
    :param single_selection: Can users select one or multiple options.
    :param end_time: Poll close time.
    :return: Poll object, Boolean (true if created).
    """
    created = False
    try:
        p = Poll.objects.get(owner=owner, name=name)
        p.question = question
        p.single_selection = single_selection
        # p.end_time = end_time
    except Poll.DoesNotExist:
        created = True
        p = Poll(
            owner=owner,
            name=name,
            question=question,
            single_selection=single_selection
            # end_time=end_time
        )
    p.save()
    return p, created


def add_poll_option(text, poll):
    """
    Add poll option object. Matching poll and option text is considered same.
    :param text: Text for the option.
    :param poll: Poll object.
    :return: Poll option object, Boolean (true, if created).
    """
    created = False
    try:
        o = PollOption.objects.get(poll=poll, text=text)
    except PollOption.DoesNotExist:
        created = True
        o = PollOption(poll=poll, text=text)
        o.save()
    return o, created


def add_poll_answers(owner, option):
    """
    Add poll answer object. Matching user and option is considered same.
    :param owner: User object.
    :param option: Chosen poll option.
    :return: Poll answer object, Boolean (true, if created).
    """
    '''
    owner = models.ForeignKey(User, related_name='poll_answers', on_delete=models.CASCADE)
    answer = models.ForeignKey(PollOption, related_name='answers', on_delete=models.CASCADE)
    '''
    created = False
    try:
        a = PollAnswer.objects.get(owner=owner, answer=option)
    except PollAnswer.DoesNotExist:
        a = PollAnswer(owner=owner, answer=option)
        a.save()
    return a, created


if __name__ == '__main__':
    print('Starting database test data population.')
    populate()
    print('Test data population completed.')
