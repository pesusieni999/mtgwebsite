"""
Views of main application are defined here.

These define what is done when routing from URLs directs here.
"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden

from .forms import RegistrationForm


__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class Index(TemplateView):
    """
    Main page for the application.
    """
    def get(self, request, **kwargs):
        return render(request, 'index.html', {})

'''
class Login(TemplateView):
    """
    Login view.
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'form': AuthenticationForm()})

    def post(self, request, **kwargs):
        users = User.objects.all()
        for u in users:
            print("Username: ", u.username)
        if request.user.is_authenticated():
            return HttpResponseRedirect('index', status=200)

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', '')
            )
            if user is not None:
                login(request, user)
                return redirect('index')
        return HttpResponseForbidden("Wrong username or password")
'''


class Register(TemplateView):
    """
    Registration view for the system.
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index')
        return render(request, 'register.html', {'form': RegistrationForm()})

    def post(self, request, **kwargs):
        if request.user.is_authenticated():
            return redirect('index')
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            # Auto login the user after registration.
            if user is not None:
                login(request, user)
            messages.info(request, "You have successfully registered.")
            return redirect('index')
        return render(request, 'register.html', {'form': form})
