"""
Define forms for Polls application.
"""

from django import forms

from .models import Poll, PollAnswer


__author__ = "pesusieni999"
__copyright__ = "Copyright 2017, MtG website Project"
__credits__ = ["pesusieni999"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "pesusieni999"
__email__ = "pesusieni999@gmail.com"
__status__ = "Development"


class PollForm(forms.ModelForm):
    """
    Form for creating and modifying Polls.
    """
    class Meta:
        model = Poll

        POLL_TYPE_CHOICES = ((True, 'Single selection'), (False, 'Multiple selection'))
        POLL_PUBLIC_CHOICES = ((True, 'Public'), (False, 'Private'))

        fields = ('name', 'question', 'single_selection', 'public')
        labels = {
            'single_selection': 'Vote type',
            'public': 'Vote publicity'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-field'}),
            'question': forms.Textarea(attrs={'class': 'form-control form-field'}),
            'public': forms.Select(
                choices=POLL_PUBLIC_CHOICES,
                attrs={'class': 'form-control form-field'}
            ),
            'single_selection': forms.Select(
                choices=POLL_TYPE_CHOICES,
                attrs={'class': 'form-control form-field'}
            ),
            # 'end_time': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
        }


class PollOptionForm(forms.Form):
    """
    Form for defining poll options (that can be voted).
    """
    text = forms.CharField(
        max_length=128,
        label="Option",
        widget=forms.TextInput(attrs={'class': 'form-control form-field'})
    )


class VoteForm(forms.Form):
    """
    Form for voting.
    """
    def __init__(self, *args, **kwargs):
        # TODO: Add initialization with polls options.
        # TODO: Need poll options, and if poll allows multiple choices.
        super(VoteForm, self).__init__(*args, **kwargs)



