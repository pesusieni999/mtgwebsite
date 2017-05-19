"""
Forms related to MtG application.
"""

from django import forms
from .models import Game, SignUp

__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class GameForm(forms.ModelForm):
    """
    Form for creating and modifying MtG game.
    """
    max_sign_ups = forms.IntegerField(min_value=0, max_value=50)

    class Meta:
        model = Game
        fields = ('format', 'time', 'location', 'max_sign_ups')
        widgets = {
            'format': forms.TextInput(attrs={'class': 'form-control form-field'}),
            'time': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
            'location': forms.TextInput(
                attrs={'class': 'form-control form-field'}
            ),
            'max_sign_ups': forms.NumberInput(
                attrs={'class': 'form-control form-field'}
            )
        }


class SignUpForm(forms.ModelForm):
    """
    Form for signing up to game.
    """
    class Meta:
        model = SignUp
        fields = ('commander', 'deck')
        widgets = {
            'commander': forms.TextInput(attrs={'class': 'form-control form-field'}),
            'deck': forms.URLInput(attrs={'class': 'form-control form-field'})
        }
