"""
Views for MtG website application.
"""

from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from django.views.generic import TemplateView
from .models import Game, SignUp
from .forms import GameForm, SignUpForm


__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class Games(TemplateView):
    def get(self, request, *args, **kwargs):
        games = Game.objects.all()
        game_form = GameForm()
        return render(
            request,
            'games.html',
            context={
                'games': games,
                'game_form': game_form
            }
        )

    def post(self, request, *args, **kwargs):
        """
        View handler for creating new game.
        :return: Success -> Redirect to game, failure -> redirect to games.
        """
        game_form = GameForm(data=request.POST)
        if not game_form.is_valid():
            games = Game.objects.all()
            return render(
                request,
                'games.html',
                context={
                    'games': games,
                    'game_form': game_form
                }
            )
        game = game_form.save(commit=False)
        game.owner = request.user
        game.save()
        messages.success(request, 'New game created.')
        return redirect(reverse('game', kwargs={'game_id': game.id}), request)


class GameView(TemplateView):
    def get(self, request, game_id=0, *args, **kwargs):
        """
        View for showing single game information.
        """
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            messages.error(request, "No such game found.")
            return redirect(reverse('games'), request)
        game_form = GameForm(instance=game)

        try:
            sign_up = SignUp.objects.get(game=game, user=request.user)
            sign_up_form = SignUpForm(instance=sign_up)
            is_signed_up = True
        except SignUp.DoesNotExist:
            sign_up_form = SignUpForm()
            is_signed_up = False
        sign_ups = SignUp.objects.filter(game=game)
        return render(
            request,
            'game.html',
            context={
                'game': game,
                'game_form': game_form,
                'sign_ups': sign_ups,
                'sign_up_form': sign_up_form,
                'is_signed_up': is_signed_up
            }
        )

    def post(self, request, game_id=0, *args, **kwargs):
        """
        View for updating existing game.
        """
        try:
            game = Game.objects.get(id=game_id, owner=request.user)
        except Game.DoesNotExist:
            messages.error(request, 'No such game found.')
            return redirect(reverse('games'), request)

        game_form = GameForm(data=request.POST, instance=game)
        if not game_form.is_valid():
            sign_ups = SignUp.objects.get(game=game)
            try:
                sign_up = SignUp.objects.get(game=game, user=request.user)
                sign_up_form = SignUpForm(instance=sign_up)
                is_signed_up = True
            except SignUp.DoesNotExist:
                sign_up_form = SignUpForm()
                is_signed_up = False
            return render(
                request,
                'game.html',
                context={
                    'game': game,
                    'game_form': game_form,
                    'sign_ups': sign_ups,
                    'sign_up_form': sign_up_form,
                    'is_signed_up': is_signed_up
                }
            )
        game = game_form.save(commit=False)
        game.owner = request.user
        game.save()
        messages.success(request, "Game information updated.")
        return redirect(reverse('game', kwargs={'game_id': game.id}), request)


class DeleteGameView(TemplateView):
    """
    View for deleting games.
    """
    def post(self, request, *args, game_id=0, **kwargs):
        try:
            game = Game.objects.get(id=game_id, owner=request.user)
        except Game.DoesNotExist:
            messages.error(request, 'No such game found.')
            return redirect(reverse('games'), request)
        game.delete()
        messages.success(request, 'Successfully deleted the game.')
        return redirect(reverse('games'), request)


class SignUpView(TemplateView):
    """
    Sign-up view.
    """
    def post(self, request, *args, game_id=0, **kwargs):
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            messages.error(request, 'No such game found.')
            return redirect(reverse('games'), request)

        try:
            sign_up = SignUp.objects.get(game=game, user=request.user)
            sign_up_form = SignUpForm(data=request.POST, instance=sign_up)
        except SignUp.DoesNotExist:
            sign_up_form = SignUpForm(data=request.POST)

        if not sign_up_form.is_valid():
            messages.error(request, 'Failed to sign-up to game.')
            return redirect(reverse('game', kwargs={'game_id': game.id}), request)

        sign_up = sign_up_form.save(commit=False)
        sign_up.game = game
        sign_up.user = request.user
        sign_up.save()
        messages.success(request, "Successfully signed up to game.")
        return redirect(reverse('game', kwargs={'game_id': game.id}), request)


class DeleteSignUpView(TemplateView):
    """
    Sign-up cancel view.
    """
    def post(self, request, *args, game_id=0, **kwargs):
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            messages.error(request, 'No cuch game found.')
            return redirect(reverse('games'), request)

        try:
            sign_up = SignUp.objects.get(game=game, user=request.user)
        except SignUp.DoesNotExist:
            messages.error(request, 'No sign-up to cancel.')
            return redirect(reverse('games'), request)

        sign_up.delete()
        messages.success(request, "Sign-up cancelled.")
        return redirect(reverse('game', kwargs={'game_id': game.id}), request)
