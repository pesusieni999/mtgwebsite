#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to populate database for testing purposes.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from django.contrib.auth.models import User

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

    # Create superusers.
    super_users_created = 0
    super_users_updated = 0
    s_user, created = add_super_user('nimba', '1234')
    if created:
        super_users_created += 1
    else:
        super_users_updated += 1

    # Print populate results.
    print('Super users created: ', super_users_created)
    print('Super users updated: ', super_users_updated)


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


if __name__ == '__main__':
    print('Starting database test data population.')
    populate()
    print('Test data population completed.')
