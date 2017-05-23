"""
Define models for Polls application.
"""

from datetime import datetime
import pytz

from django.db import models
from django.contrib.auth.models import User


__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class Poll(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name='pollapp', on_delete=models.CASCADE)
    question = models.CharField(max_length=1028)
    single_selection = models.BooleanField(default=True)
    user_closed = models.BooleanField(default=False)
    public = models.BooleanField(default=True)

    # Time information about poll object itself.
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    # end_time = models.DateTimeField()

    def get_answers(self):
        """
        Get answers to this poll.
        :return: Queryset containing this pollapp results.
        """
        return PollAnswer.objects.filter(answer__poll=self)

    def get_answer_count(self):
        """
        Get count of poll answers.
        :return: Count of poll answers.
        """
        return PollAnswer.objects.filter(answer__poll=self).count()

    def is_closed(self):
        """
        Check is poll closed.
        :return: Return true if poll has been closed by owner or time closed.
        """
        return self.user_closed  # or self.end_time > datetime.now(tz=pytz.utc)

    def is_edited(self):
        """
        Check has poll been edited.
        :return: True if poll has been edited.
        """
        return self.last_edited > self.created

    def get_poll_options(self):
        return PollOption.objects.all().filter(poll=self)


class PollOption(models.Model):
    text = models.CharField(max_length=512)
    poll = models.ForeignKey(Poll, related_name='poll_options', on_delete=models.CASCADE)

    def get_answer_count(self):
        """
        Get answer number for this poll option.
        :return: Integer showing number of poll option choices.
        """
        return PollAnswer.objects.filter(answer=self).count()


class PollAnswer(models.Model):
    owner = models.ForeignKey(User, related_name='poll_answers', on_delete=models.CASCADE)
    answer = models.ForeignKey(PollOption, related_name='answers', on_delete=models.CASCADE)

    @staticmethod
    def has_user_voted(user, poll):
        """
        Check has the user voted in given poll.
        :param user: User object to check vote.
        :param poll: Poll object from which to check.
        :return: True if user has voted in given poll.
        """
        if user.is_authenticated():
            return PollAnswer.objects.filter(owner=user, answer__poll=poll).exists()
        else:
            return False
