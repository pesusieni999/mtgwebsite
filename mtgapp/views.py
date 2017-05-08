"""
Views for MtG website application.
"""

from django.shortcuts import render
from django.views.generic import TemplateView


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
        return render(request, 'games.html', {})
