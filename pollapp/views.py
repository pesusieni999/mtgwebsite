"""
Define views for Polls application.
"""

from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView
from django.forms import formset_factory

from .models import Poll, PollAnswer, PollOption
from .forms import PollForm, PollOptionForm, VoteForm

__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class Polls(TemplateView):
    def get(self, request, *args, **kwargs):
        polls = Poll.objects.all()
        poll_form = PollForm()
        return render(
            request,
            'polls.html',
            context={
                'polls': polls,
                'poll_form': poll_form
            }
        )

    def post(self, request, *args, **kwargs):
        """
        View handler for creating new polls.
        :return: Success -> Redirect to poll, failure -> redirect to polls.
        """
        poll_form = PollForm(data=request.POST)
        if not poll_form.is_valid():
            polls = Poll.objects.all()
            return render(
                request,
                'polls.html',
                context={
                    'polls': polls,
                    'poll_form': poll_form
                }
            )
        poll = poll_form.save(commit=False)
        poll.owner = request.user
        poll.save()
        messages.success(request, 'New poll created.')
        return redirect(reverse('poll', kwargs={'poll_id': poll.id}), request)


class PollView(TemplateView):
    def get(self, request, *args, poll_id=0, **kwargs):
        """
        View for showing single poll information.
        :return: Render poll view (if such poll exists).
        """
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            messages.error(request, "No such poll found.")
            return redirect(reverse('polls'), request)
        poll_form = PollForm(instance=poll)
        poll_options = PollOption.objects.filter(poll=poll.id)
        has_voted = PollAnswer.has_user_voted(request.user, poll)
        return render(
            request,
            'poll.html',
            context={
                'poll': poll,
                'poll_form': poll_form,
                'poll_options': poll_options,
                'has_voted': has_voted
            }
        )

    def post(self, request, poll_id=0, *args, **kwargs):
        """
        View for updating single poll.
        """
        try:
            poll = Poll.objects.get(id=poll_id, owner=request.user)
        except Poll.DoesNotExist:
            messages.error(request, 'No such poll found.')
            return redirect(reverse('polls'), request)
        poll_form = PollForm(data=request.POST, instance=poll)
        if not poll_form.is_valid():
            has_voted = PollAnswer.has_user_voted(user, poll)
            return render(
                request,
                'poll.html',
                context={
                    'poll': poll,
                    'poll_form': poll_form,
                    'has_voted': has_voted
                }
            )
        poll = poll_form.save(commit=False)
        poll.owner = request.user
        poll.save()
        messages.success(request, 'Poll information updated.')
        return redirect(reverse('poll', kwargs={'poll_id': poll.id}), request)


class DeletePoll(TemplateView):
    """
    View for deleting polls.
    """
    def post(self, request, *args, poll_id=0, **kwargs):
        try:
            poll = Poll.objects.get(id=poll_id, owner=request.user)
        except Poll.DoesNotExist:
            messages.error(request, 'No such poll found.')
            return redirect(reverse('games'), request)
        poll.delete()
        messages.success(request, 'Successfully deleted the poll.')
        return redirect(reverse('polls'), request)


class VoteView(TemplateView):
    """
    Vote view.
    """
    def post(self, request, *args, poll_id=0, **kwargs):
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            messages.error(request, 'No such poll found.')
            return redirect(reverse('polls'), request)

        try:
            vote = PollAnswer.objects.get(
                answer__poll=poll,
                owner=request.user
            )
            vote_form = VoteForm(data=request.POST, instance=vote)
        except PollAnswer.DoesNotExist:
            vote_form = VoteForm(data=request.POST)

        if not vote_form.is_valid():
            messages.error(request, 'Failed to vote.')
            return redirect(
                reverse('poll', kwargs={'poll_id': poll.id}),
                request
            )

        vote = vote_form.save(commit=False)
        vote.owner = request.user
        vote.save()
        messages.success(request, "Successfully voted.")
        return redirect(reverse('poll', kwargs={'poll_id': poll.id}), request)


class DeleteVote(TemplateView):
    """
    Delete vote view.
    """
    def post(self, request, *args, poll_id=0, **kwargs):
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            messages.error(request, 'No such pol found.')
            return redirect(reverse('polls'), request)

        try:
            vote = PollAnswer.objects.get(
                answer__poll=poll,
                owner=request.user
            )
        except PollAnswer.DoesNotExist:
            messages.error(request, 'No vote to delete.')
            return redirect(reverse('polls'), request)

        vote.delete()
        messages.success(request, "Vote deleted.")
        return redirect(reverse('poll', kwargs={'poll_id': poll.id}), request)


class PollOptionsView(TemplateView):
    """
    View for adding, updating and deleting poll options.
    """
    def get(self, request, *args, poll_id=0, **kwargs):
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            messages.error(request, 'No such pol found.')
            return redirect(reverse('polls'), request)

        options = PollOption.objects.filter(poll=poll)
        return render(
            request,
            'polloptions.html',
            context={
                'poll': poll,
                'poll_options': options
            }
        )

