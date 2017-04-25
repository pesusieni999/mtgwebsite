"""
Generic forms of main application are defined here.
"""

from django import forms
from django.contrib.auth.models import User

__author__ = "Ville Myllynen"
__copyright__ = "Copyright 2017, Ohsiha Project"
__credits__ = ["Ville Myllynen"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ville Myllynen"
__email__ = "ville.myllynen@student.tut.fi"
__status__ = "Development"


class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    tos_agreement = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'lg-checkbox'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-field'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-field',
                'placeholder': 'email@example.com'
            }),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-field'})
        }