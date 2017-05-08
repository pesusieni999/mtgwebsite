"""
Generic forms of main application are defined here.
"""

from django import forms
from django.contrib.auth.models import User

__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    #tos_agreement = forms.BooleanField(
    #    required=True,
    #    widget=forms.CheckboxInput(attrs={'class': 'lg-checkbox'})
    #)

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-field'}),
            #'email': forms.EmailInput(attrs={
            #    'class': 'form-control form-field',
            #    'placeholder': 'email@example.com'
            #}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-field'})
        }